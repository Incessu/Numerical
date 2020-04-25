def f(x):
    return x * x * x - 7 * x * x + 14 * x - 6

print("Enter the Interval Limits [a,b]")
a = int(input())  ## Interval Limits [a,b]
b = int(input())
c = (a + b) / 2

if f(a) * f(b) < 0:
    print("Bisection Avaliable in [{},{}]".format(a, b))
else:
    print("Bisection Not Avaliable ")

while abs(f(c)) > 0.000001:
    print(c)
    if f(a)*f(c) < 0:
        a = a
        b = c
        c = (a + c) / 2
    elif f(c)*f(b) < 0:
        a = c
        b = b
        c = (c + b) / 2