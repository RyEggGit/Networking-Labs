import math
import random

def exponential_distribution(lam: int) -> float:
    U = random.random()
    return (-1/lam) * math.log(1 - U)

if __name__ == '__main__':
    RATE_PARAMETER = 75
    EPOCH = 1000

    # Generate samples
    samples: list[float] = [exponential_distribution(RATE_PARAMETER) for _ in range(EPOCH)]

    # Calculate mean and variance
    mean = sum(samples) / EPOCH
    variance = sum([(x - mean) ** 2 for x in samples]) / EPOCH

    # Expected values for comparison
    expected_mean = 1 / RATE_PARAMETER
    expected_variance = (1 / RATE_PARAMETER) ** 2

    print(f'Mean: {mean:.16f} (expected: {expected_mean:.16f})')
    print(f'Variance: {variance:.16f} (expected: {expected_variance:.16f})')




    

    

