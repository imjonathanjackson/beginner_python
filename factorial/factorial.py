def factorial(num):
    count = 1
    for i in reversed(range(0, num, 1)):
        count = count * num
        num -= 1
    print(count)

fact = input("Enter number to calculate factorial of: ")
factorial(int(fact))
