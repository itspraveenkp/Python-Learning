f = open("Note.txt","rt")
content = f.read()
print(content)

print("----------------------------------------------------")

f = open("Note.txt","rt")
contents = f.readline()
print(contents)

print("----------------------------------------------------")

f = open("Note.txt","rt")
contentss = f.readlines()
print(contentss)

print("----------------------------------------------------")

f = open("Note.txt")
contenting = f.read()
for line in f:
    print(contenting, end="")
print(contenting)

