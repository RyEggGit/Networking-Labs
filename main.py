import math
import random
from LoadingBar import LoadingBar
from heapq import heappop, heappush
import csv


class ExponentialDistribution:
    def generate(self, parameter: float) -> float:
        return (-1/parameter) * math.log(1 - random.random())

    def simulate(self) -> None:
        RATE_PARAMETER = 75
        EPOCH = 1000

        # Generate samples
        samples: list[float] = [self.generate(RATE_PARAMETER) for _ in range(EPOCH)]

        # Calculate mean and variance
        mean = sum(samples) / EPOCH
        variance = sum([(x - mean) ** 2 for x in samples]) / EPOCH

        # Expected values for comparison
        expected_mean = 1 / RATE_PARAMETER
        expected_variance = (1 / RATE_PARAMETER) ** 2

        print(f'Mean: {mean:.16f} (expected: {expected_mean:.16f})')
        print(f'Variance: {variance:.16f} (expected: {
              expected_variance:.16f})')


class Event:
    """Base class for an event in DES"""

    def __init__(self, event_time: float, event_type: str):
        self.event_time = event_time
        self.event_type = event_type

    def __lt__(self, other: "Event") -> bool:
        return self.event_time < other.event_time


class ArrivalEvent(Event):
    """Packet arrival event"""

    def __init__(self, event_time: float, packet_length: float):
        super().__init__(event_time, "arrival")
        self.packet_length = packet_length


class DepartureEvent(Event):
    """Packet departure event"""

    def __init__(self, event_time: float):
        super().__init__(event_time, "departure")


class ObserverEvent(Event):
    """Observer event to check queue status"""

    def __init__(self, event_time: float):
        super().__init__(event_time, "observer")


class QueueSystem:
    def __init__(self, simulation_time: float, transmission_rate: float, queue_utilization: float, packet_length: float, buffer_size: float = float('inf'),):
        self.transmission_rate = transmission_rate
        self.buffer_size = buffer_size
        self.simulation_time = simulation_time
        self.packet_length = packet_length

        self.queue: list[float] = []  # Queue of packet lengths
        self.event_list: list[Event] = []  # Priority queue for events
        self.time = 0  # Current simulation time
        self.Na = 0  # Number of packet arrivals
        self.Nd = 0  # Number of packet departures
        self.No = 0  # Number of observer events
        self.total_packets_in_queue = 0
        self.idle_time = 0
        self.last_event_time = 0
        self.packets_lost = 0

        self.arival_param = (queue_utilization *
                             transmission_rate) / packet_length
        self.random = ExponentialDistribution()

    def schedule_event(self, event: Event):
        """Adds an event to the event list (priority queue)"""
        heappush(self.event_list, event)

    def generate_arrival(self):
        """Generates the next packet arrival based on the arrival process"""
        arrival_time = self.time + self.random.generate(self.arival_param)
        packet_length = self.random.generate(
            self.packet_length) * self.transmission_rate * 5
        return ArrivalEvent(arrival_time, packet_length)

    def generate_observer(self):
        """Generates an observer event"""
        observer_time = self.time + self.random.generate(self.arival_param) / 5
        return ObserverEvent(observer_time)

    def handle_arrival(self, event: ArrivalEvent):
        """Handles an arrival event"""
        self.Na += 1
        if len(self.queue) < self.buffer_size:
            self.queue.append(event.packet_length)
            if len(self.queue) == 1:  # Queue was idle, schedule a departure
                self.idle_time += self.time - self.last_event_time
                service_time = event.packet_length / self.transmission_rate
                departure_time = self.time + service_time
                self.schedule_event(DepartureEvent(departure_time))
        else:
            self.packets_lost += 1  # Packet dropped because the buffer is full

    def handle_departure(self, event: DepartureEvent):
        """Handles a departure event"""
        self.Nd += 1
        if self.queue:
            self.queue.pop(0)  # Remove the packet from the queue
            if self.queue:  # If there are still packets in the queue, schedule the next departure
                next_packet_length = self.queue[0]
                service_time = next_packet_length / self.transmission_rate
                departure_time = self.time + service_time
                self.schedule_event(DepartureEvent(departure_time))

    def handle_observer(self, event: ObserverEvent):
        """Handles an observer event"""
        self.No += 1
        queue_length = len(self.queue)
        self.total_packets_in_queue += queue_length

    def calculate_metrics(self):
        """Calculates performance metrics"""
        print(f"Total packets in queue: {self.total_packets_in_queue}")

        E_N = self.total_packets_in_queue / self.No if self.No > 0 else 0
        P_IDLE = self.idle_time / self.simulation_time
        P_LOSS = self.packets_lost / self.Na if self.Na > 0 else 0
        return E_N, P_IDLE, P_LOSS

    def run_simulation(self):
        arrival = self.generate_arrival()
        self.schedule_event(arrival)
        observer = self.generate_observer()
        self.schedule_event(observer)

        """Runs the DES simulation"""
        self.time = 0
        while self.event_list and self.time < self.simulation_time:
            # Get the next event
            event = heappop(self.event_list)
            if event.event_time > self.simulation_time:
                break
            self.time = event.event_time
            
            if isinstance(event, ArrivalEvent):
                self.handle_arrival(event)
                arrival = self.generate_arrival()
                self.schedule_event(arrival)
                self.last_event_time = self.time
            elif isinstance(event, DepartureEvent):
                self.handle_departure(event)
                self.last_event_time = self.time
            elif isinstance(event, ObserverEvent):
                self.handle_observer(event)
                observer = self.generate_observer()
                self.schedule_event(observer)

        self.idle_time += self.simulation_time - self.last_event_time
        print()
        return self.calculate_metrics()


if __name__ == "__main__":
    utilizations = list(range(25, 95))
    E_N_values: list[float] = []
    P_IDLE_values: list[float] = []

    for row in utilizations:
        queue_system = QueueSystem(simulation_time=1000, transmission_rate=1_000_000,
                                   packet_length=2000, queue_utilization=row / 100, buffer_size=float('inf'))

        E_N, P_IDLE, P_LOSS = queue_system.run_simulation()

        E_N_values.append(E_N)
        P_IDLE_values.append(P_IDLE * 100)  # Convert to percentage

        print(f"Utilization: {row / 100}")
        print(f"Average number of packets in queue (E[N]): {E_N}")
        print(f"Proportion of idle time (P_IDLE): {P_IDLE * 100:.2f}%")
        print(f"Probability of packet loss (P_LOSS): {P_LOSS * 100:.2f}%")
        print()

    with open('simulation_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Utilization', 'E[N]', 'P_IDLE'])
        for i in range(len(utilizations)):
            writer.writerow([utilizations[i], E_N_values[i], P_IDLE_values[i]])
