def fibonnaci(n):
    n = int (n)
    a = 0
    b = 1
    c = 0
    while n > 1:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

fib = input("Enter the position in the Fibonnaci Series you would like to calculate? ")
print(fibonnaci(fib))
