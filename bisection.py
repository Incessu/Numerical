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
    print("\nReached Root is : %0.8f" % c)
    print("\nReach the Root in %d" % n)


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