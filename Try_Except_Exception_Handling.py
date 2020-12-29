print("Please Enter Num1:")
num1 = input()
print("Please Enter num2:")
num2 = input()

try:
    num3 = int(num1) + int(num2)
    print("The Addition of num1 and num2 :"
    ,num3)
except Exception as e:
    print(e)

print("Your next printed Value")

