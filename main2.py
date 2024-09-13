def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter a number to find the fibonacci for: "))
print("The fibonacci placeholder for your number,",n, "is" , fibonacci(n))

for i in range(0, n+1):
    print(fibonacci(i), end = ", ")

