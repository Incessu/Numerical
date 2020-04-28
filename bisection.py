import matplotlib.pyplot as plt
import numpy as np

## Defining Function
def f(x):
    return x**3 - 5*x - 8

## Bisection Method Algorithm
def bisection(a, b, error,xson,yson):
    c = (a + b) / 2
    iteration = 1
    print("\n--- BISECTION METHOD ---\n")
    while abs(f(c)) > error:
        c = (a + b) / 2
        print('Iteration-{}, c = {} and f(c) = {}' .format (iteration, c, abs(f(c))))

        if f(a) * f(c) < 0:
            b = c
            xson.append(c)
            yson.append(f(c))
        elif f(c) * f(b) < 0:
            a = c
            xson.append(c)
            yson.append(f(c))
        else:
            xson.append(c)
            yson.append(f(c))
            break
        iteration = iteration + 1
    print('\nReach the Root on Iteration-{} the root is: {}' .format (iteration, c))

## Input
print("\nEnter the Interval Limits [a,b] and Tolerable Error\n")
a = float(input('a: '))
b = float(input('b: '))
error = float(input('Tolerable Error: '))

## Graph Elemnt Lists
xson = []
yson = []

## Bisection Method Condition Check and Implement Method
if f(a) * f(b) < 0:
    bisection(a, b, error, xson, yson)
else:
    print("Bisection Unavailable in [%d,%d]" % (a, b))
    print('Try Again with different Interval Limits [a,b].')

##Graph of Bisection Method for Visualizing
x = np.arange(a, b, 0.001)
y = (f(x))

plt.title("Bisection Method on f(x)")

plt.plot(x, y, label="f(x)")
plt.plot(xson, yson , '-o', label="Bisection Iterations")

plt.xlabel('x')
plt.ylabel('y')

plt.grid()
plt.legend()
plt.show()