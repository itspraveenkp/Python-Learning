# Dictionary is nothing but key value paire
D1 = [] # list
D2 = () # tuple
D3 = {} # Dictionary

# print(type(D3)) # this is use for check type

# We are going to defind Dictionary

Dictionari = {"Praveen":"Biryani","Rajendra":"Roti","Ravi":"Food","Sujeet":"halwa",
"Ajay" : {"Morning":"Beri","AfterNoon":"Puri","Night" : "Roti-bhat"}} # We can add also inside dictionary to dict

# print(Dictionari["Praveen"])
# print(Dictionari["Ajay"])
# print(Dictionari["Ajay"] ["Morning"])

# We want to update our dictionary 
# First Method

# Dictionari["Raj"] = "Flower"
# print(Dictionari)

# Second Method
# Dictionari.update ({"Raj":"Mango"})
# print(Dictionari)

# We are Going to delete someone from Dictionary
# del Dictionari["Rajendra"]
# print(Dictionari)

#check values keys and values.
# print(Dictionari.keys())
# print(Dictionari.values())

while True:
    List1 = {'Ravi':'Prajapati','Akshay':'Sawant','Ankita':'Pednekar','Komal':'Bhoi','Praveen':'Prajapati'}

# print(type(List1))
    name = input("Enter Your Name and check Your second Name:")
    print(List1[name])




