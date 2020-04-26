import matplotlib.pyplot as plt
import numpy as np

## Defining Function
def f(x):
    return x ** 3 - 5 * x - 9

## Bisection Method
def bisection(a, b, error):
    c = (a + b) / 2
    n = 1  ##
    print("\n--- BISECTION METHOD ---\n")
    while abs(f(c)) > error:
        c = (a + b) / 2
        print('Iteration-%d, c = %0.8f and f(c) = %0.6f' % (n, c, abs(f(c))))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        n = n + 1
    print('\nReach the Root Iteration-%d the root is: %0.8f' % (n,c))


## Input [a,b] and Tolerable Error
print("\nEnter the Interval Limits [a,b] and Tolerable Error")
a = float(input('a: '))
b = float(input('b: '))
error = float(input('Tolerable Error: '))

## Bisection Status Check and Start Method
if f(a) * f(b) > 0:
    print("Bisection Avaliable in [%d,%d]" % (a, b))
    print('Try Again with different Interval Limits [a,b].')
else:
    bisection(a, b, error)
x = np.arange(a,b,0.0000001)
y = abs(f(x))
plt.title("Bisection Method on f(x)")
plt.plot(x,y)
plt.show()