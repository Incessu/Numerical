import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

## Defining Function
def f(x):
    return x**3 - 5*x - 8

## Defining derivative of f(x)
def g(x):
    return 3*x**2 - 5


## Newton Raphson Method Algorithm
def newtonRaphson(x0, error, xson, yson):
    x1 = x0 - f(x0) / g(x0)
    print("\n---NEWTON RAPHSON METHOD ---\n")
    iteration = 1
    while abs(f(x1)) > error:
        if g(x0) == 0.0:
            print("ERROR : Divide by zero!")
            break

        x1 = x0 - f(x0) / g(x0)
        xson.append(x1)
        yson.append(f(x1))
        print("Iteration-%d, x1 = %0.8f and f(x1) = %0.6f" % (iteration, x1, abs(f(x1))))
        x0 = x1
        iteration = iteration + 1

    print("\nReach the Root Iteration-%d the root is: %0.8f" % (iteration, x1))

## Input
print("\nEnter the Initial Value and Tolerable Error\n")
x0 = float(input("Enter Initial Value (x0): "))
error = float(input("Tolerable Error: "))

## Graph Elemnt Lists
xson = []
yson = []

##Implementing Newton Raphson Method
newtonRaphson(x0, error, xson, yson)

##Graph of Bisection Method for Visualizing
x = np.arange(-x0, x0, 0.001)
y = (f(x))

plt.title("Newton Raphson Method on f(x)")

plt.plot(x, y, label="f(x)")
plt.plot(xson, yson , '-o', label="Newton Iterations")

plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.legend()
plt.show()