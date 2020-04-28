import matplotlib.pyplot as plt
import numpy as np

## Defining Function
def f(x):
    return x**3 - 5*x - 8

##Secant Method Algorithm
def secant(x0, x1, error, xson, yson):
    x2 = x0 - (x0-x1) * f(x0) / (f(x0)-f(x1))
    print('\n--- SECANT METHOD ---\n')
    iteration = 1

    while abs(f(x2)) > error:
        if f(x0) == f(x1):
            print('ERROR : Divide by zero!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        xson.append(x2)
        yson.append(f(x2))
        print('Iteration-%d, x2 = %0.8f and f(x2) = %0.6f' % (iteration, x2, abs(f(x2))))
        x0 = x1
        x1 = x2
        iteration = iteration + 1

    print('\nReach the Root Iteration-%d the root is: %0.8f' % (iteration, x2))

## Input
print("\nEnter the Initial Values and Tolerable Error\n")
x0 = float(input('Enter Initial Value (x0): '))
x1 = float(input('Enter Initial Value (x1): '))
error = float(input('Tolerable Error: '))

## Graph Elemnt Lists
xson = []
yson = []

## Implementing Secant Method
secant(x0, x1, error, xson, yson)

##Graph of Bisection Method for Visualizing
x = np.arange(x0, x1, 0.001)
y = (f(x))

plt.title("Secant Method on f(x)")

plt.plot(x, y, label="f(x)")
plt.plot(xson, yson , '-o', label="Secant Iterations")

plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.legend()
plt.show()