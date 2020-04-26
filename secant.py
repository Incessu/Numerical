# Defining Function
def f(x):
    return x ** 3 - 5 * x - 9


# Implementing Secant Method
def secant(x0, x1, error):
    x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    n = 1
    condition = True
    while abs(f(x2)) > error:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.8f and f(x2) = %0.6f' % (n, x2, abs(f(x2))))
        x0 = x1
        x1 = x2
        n = n + 1

    print('\nReach the Root Iteration-%d the root is: %0.8f' % (n, x2))


# Note: You can combine above three section like this
x0 = float(input('Enter First Guess: '))
x1 = float(input('Enter Second Guess: '))
error = float(input('Tolerable Error: '))

# Starting Secant Method
secant(x0, x1, error)