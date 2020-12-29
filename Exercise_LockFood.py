# Health Management System
# 3 Client harry Rohar, Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# Write a function that when execute takes as input client name
#one more function to retrieve exercise or food for any client 

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k == 1:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if(c == 1):
            value = input("Type Here....\n ")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+ ": " + value + "\n")
            print("Successfully Written")
        elif(c == 2):
            value = input("Type Here....\n")
            with open("harry-food","a") as op:
                op.write(str([str(gettime())])+ ": "+value+ "\n")
            print("successfully Written")

    elif k == 2:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if(c == 1):
            value = input("Type Here....\n ")
            with open("Rohan-ex.txt","a") as op:
                op.write(str([str(gettime())])+ ": " + value + "\n")
            print("Successfully Written")
        elif(c == 2):
            value = input("Type Here....\n")
            with open("Rohar-food","a") as op:
                op.write(str([str(gettime())])+ ": "+value+ "\n")
            print("successfully Written")

    elif k == 1:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if(c == 1):
            value = input("Type Here....\n ")
            with open("hammad-ex.txt","a") as op:
                op.write(str([str(gettime())])+ ": " + value + "\n")
            print("Successfully Written")
        elif(c == 2):
            value = input("Type Here....\n")
            with open("hammad-food","a") as op:
                op.write(str([str(gettime())])+ ": "+value+ "\n")
            print("successfully Written")
    else:
        print("Please Enter Valid input (1(harry),2(rohan),3(hammad)")

# print(take(2))

def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for Execise and 2 for Food"))
        if(c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k == 1:
        c = int(input("Enter 1 for Execise and 2 for Food"))
        if(c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i,end="")

    elif k == 1:
        c = int(input("Enter 1 for Execise and 2 for Food"))
        if(c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        print("Please Enter valid input (harry, rohan,hammad)")
    
print("Health management System: ")
a = int(input("Press 1 for log the value and 2 for Retrieve"))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan and 3 for hammad"))
    take(b)
else:
    b= int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)