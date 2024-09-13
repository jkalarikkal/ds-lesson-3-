def factorial(n):
    #for base case (stopping)
    if n == 1 or n ==0:
        return 1
    #recurring
    else:
        return n*factorial(n-1)

n = int(input("Please enter a number: "))
print("Factorial of", n,"is:", factorial(n))