# ----------------------operators In python-------------------#
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Indentity operators
# membership operators
# bitwise operators

#----------------- Arithmetic operators----------------#
print("#----------------- Arithmetic operators----------------#")

print("5 + 6 is :",5+6)
print("5 - 6 is :",5-6)
print("5 * 6 is :",5*6)
print("5 / 6 is :",5/6)
print("5 % 6 is :",5%6)
print("5 // 6 is :",5//6) # Return integer value, means Actual count before dot.
print("5 ** 6 is :",5**6) #Xponetional operator

#------------------ Assignment operators---------------------#
print("#------------------ Assignment operators---------------------#\n")

x = 5
print(x)
x += 10 # this operator just add count in created variable means add value 5 + 10 = 15
print(x)
x -= 10
print(x)
x /= 10
print(x)
x *= 10
print(x)
x %=7
print(x)

# ---------------------Comparison operators--------------------

print("# ---------------------Comparison operators--------------------")
i=5
print(i==5)
print(i!=5)
print(i>5)
print(i>=5)
print(i<5)
print(i<=5)

# ---------------------Logical operators--------------------
print("# ---------------------Logical operators--------------------\n")

a =True
b = False
print(a and a)
print(a and b)
print(b and b)
print(b and a)

print(a or a)
print(a or b)
print(b or b)
print(b or a)

# ---------------------Identity operators--------------------
print("# ---------------------Identity operators--------------------\n")

t = True
f= False
print(t is not f)
print(t is t)
print(f is t)
print(f is not f)
print(f is f)

# ---------------------membership operators--------------------
print("# ---------------------membership operators--------------------\n")

list = [13,3,2,39,33,35,32]
print(32 in list)
print(324 not in list)

# ---------------------BitWise operators--------------------
print("# ---------------------BitWise operators--------------------\n")

# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 1)
print(0 | 1)
print(0 | 3)
print(0 & 3)

