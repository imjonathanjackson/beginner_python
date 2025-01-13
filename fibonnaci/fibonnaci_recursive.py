def fibonnaci_recursive(n):
    #Convert string input to int
    n = int (n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci_recursive(n-2) + fibonnaci_recursive(n-1)

fib = input("Enter the position in the Fibonnaci Series you would like to calculate? ")
print(fibonnaci_recursive(fib))
