f = open("Note2.txt","a")
a = f.write("Praveen File appending text \n")
print(a)
f.close()


f = open("Note2.txt","r+") # for read and write both
print(f.read())
f.write("Thank you")