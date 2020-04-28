import matplotlib.pyplot as plt
import numpy as np

## Defining Function
## Defining Function
def f(x):
    return x ** 3 - 5 * x - 9

## Calculating f(x) = 0 -> x = g(x)
def g(x):
    return (x ** 3 - 9) / 5

## Fixed Point Iteration Method Algorithm
def fixedPointIteration(x0, error, xson, yson):
    x1 = g(x0)
    print('\n--- FIXED POINT ITERATION METHOD ---\n')
    iteration = 1
    while abs(f(x1)) > error:
        x1 = g(x0)
        xson.append(x0)
        yson.append(f(x0))
        print('Iteration-%d, x1 = %0.8f and f(x1) = %0.6f' % (iteration, x1, abs(f(x1))))
        x0 = x1
        iteration = iteration + 1

    print('\nReach the Root on Iteration-%d the root is: %0.8f' % (iteration, x1))

## Input
print("\nEnter the Initial Value and Tolerable Error\n")
x0 = float(input('Initial Value (x0): '))
error = float(input('Tolerable Error: '))

## Graph Elemnt Lists
xson = []
yson = []

## Implement Fixed Point Iteration Method
fixedPointIteration(x0, error, xson, yson)

##Graph of Bisection Method for Visualizing
x = np.arange(-x0, x0, 0.001)
y = (f(x))

gx = np.arange(-x0, x0, 0.001)
gy = (g(gx))

plt.title("Fixed Point Iteratio Method on f(x)")

plt.plot(x, y, label="f(x)")
plt.plot(gx, gy, label="g(x)")
plt.plot(xson, yson , '-o', label="Fixed Point Iterations")
plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.legend()
plt.show()