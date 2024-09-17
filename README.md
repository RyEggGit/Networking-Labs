# Networking-Labs

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
