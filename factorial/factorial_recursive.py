def factorial_recursive(n):
  #Convert string input to integer
  n = int (n)
  #Base Case
  if n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)
  
fact = input("Enter number to calculate factorial of: ")
print(factorial_recursive(fact))
