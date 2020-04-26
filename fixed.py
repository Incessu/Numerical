import matplotlib.pyplot as plt
import numpy as np

## Defining Function
def f(x):
    return x ** 3 - 5 * x - 9

# Calculating f(x) = 0 -> x = g(x)
def g(x):
    return (x ** 3 - 9)/5

##Fixed Point Iteration Method
def fixedPointIteration(x0, error):
    x1 = g(x0)
    print('\n\n*** FIXED POINT ITERATION ***')
    n = 1
    while abs(f(x1)) > error:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.8f and f(x1) = %0.6f' % (n, x1, abs(f(x1))))
        x0 = x1
        n = n + 1

    print('\nReach the Root Iteration-%d the root is: %0.8f' % (n,x1))

## Input Inıtıal Guess and Tolerable Error
x0 = float(input('Initial Value: '))
error = float(input('Tolerable Error: '))

# Fixed Point Iteration Method
fixedPointIteration(x0,error)

x = np.arange(x0,3,0.0000001)
y = abs(f(x))
plt.title("Bisection Method on f(x)")
plt.plot(x,y)
plt.show()