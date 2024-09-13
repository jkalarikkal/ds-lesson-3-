def power(n, u):
    if u == 0 or n == 1:
        return 1
    elif n == 0:
        return 0
    elif u == 1:
        return n
    else:
        return n*power(n, u - 1)


n = int(input("Enter a base number: "))
u = int(input("Enter a number for your prev num to be put to the power of: "))

print("The answer is: ", power(n,u))
