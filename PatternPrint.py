print("How many row want to print : ")
userinputone = int(input())
print("type 1 or 0 ")
userinputtwo = int(input())
new = bool(userinputtwo)
if new == True:
    for i in range(1,userinputone+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
elif new == False:
    for i in range(userinputone,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
