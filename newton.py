# Defining Function
def f(x):
    return x ** 3 - 5 * x - 9

# Defining derivative of function
def g(x):
    return 3 * x ** 2 - 5


# Implementing Newton Raphson Method
def newtonRaphson(x0, error):
    x1 = x0 - f(x0) / g(x0)
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    n = 1
    while abs(f(x1)) > error:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.8f and f(x1) = %0.6f' % (n, x1, abs(f(x1))))
        x0 = x1
        n = n + 1

    print('\nReach the Root Iteration-%d the root is: %0.8f' % (n,x1))

x0 = float(input('Enter Guess: '))
error  = float(input('Tolerable Error: '))

# Starting Newton Raphson Method
newtonRaphson(x0, error)