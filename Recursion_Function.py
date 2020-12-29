# def Print2(str1):
#     print("This is " + str1)

# Print2("harry")

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the Number : "))
print(fibonacci(number))