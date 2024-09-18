# Networking-Labs
*Not really meant to be public but want to easily access over ssh*

## Question 1
*Write a Python function that receives λ as one of its arguments and that returns a single random sample
drawn from an exponential random distribution. Using this function, write a short piece of Python code
to generate 1000 exponential random variables with λ=75. What is the mean and variance of the 1000
random variables you generated? Do they agree with the expected value and the variance of an
exponential random variable with λ=75? Your values will not be exact. Why not? Note: if you do not
know what you are expecting to see, you will need to look it up.*

| **Statistic** | **Computed Value**       | **Expected Value**        |
|---------------|---------------------------|---------------------------|
| Mean          | 0.0133048956165309        | 0.0133333333333333        |
| Variance      | 0.0001716209800562        | 0.0001777777777778        |

They can't be exact because we are running a finite amount of experiments on a random variables. As we increase
the number of experiments we can got close the theoretical expected and variance but will never be able to truly reach it.

## Question 2
*Build your simulator for an M/M/1. Explain in words how you compute the performance metrics E[n] and
P_IDLE. Do not show code.*

1. To computed E[N], the simulator needs to keep count of two variables, the total number of packets in the queue and the number of observers. Since the observer events happend much faster than the arrival/departure events we can use those times to accurately acheieve the average load on the queue. During each observer event the simulator adds the current packets in the queue to a total number of packets in the queue. Divide the sum by the number of times that it has been counted should be perfect to get the average size of the queue.

2. To compute P_IDLE, the simulator needs to keep track of its total time idling and divide it by the length of the simulation. During the simulation, when a packet arrival occurs, the simulator checks if the queue was previously empty. If it was empty it simply subtracts the current time - the last departure. 

## Question 3
*The packet length will follow an exponential distribution with an average of L = 2000 bits. Assume that C
= 1Mbps. Use your simulator to obtain the following graphs. Plot them on separate figures.

1.*E[N], the average number of packets in the queue as a function of ρ (for 0.25 < ρ< 0.95, step size 0.1).*
2. *P_IDLE, the proportion of time the system is idle as a function of ρ (for 0.25 < ρ< 0.95, step size 0.1).*

*Explain the trends in both graphs*

1. As you increate the queue utilization it makes sense that the average number of packets in the queue increases. 

