print("----------------------------------------------------------")

# a = 5
# b = 9
# c = sum((a,b))
# print(c)

def Function1():
    """This is Function 1 """
    print("Hello World you are function1 !!")

# print(Function1())
Function1() #Function we can use multiple times


#//////////////////////// Input type function ///////////////


print("----------------------------------------------------------")

def Function2(a , b):
    """This is Function 2 """
    print("Hello You are in function2 :", a+b)

Function2(13 , 16)

#//////////////////////// Store in variable = Input type function ///////////////
print("----------------------------------------------------------")


def function3(d, e):
    """This is Function 3 """
    print("Hello World !! you are in function3")
    average = (d + e)/2

    # print(average)
    return average

v = function3(5,5)
print(v)

print(Function1.__doc__)
print(Function2.__doc__)
print(function3.__doc__)