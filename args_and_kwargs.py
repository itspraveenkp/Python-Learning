# def function_Name_Print(a,b,c,d):
#     print(a,b,c,d)

# function_Name_Print("praveen","Harry","rohan","skilf")


def Function_argsss(normal,*args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\n Now i would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
        
har=["harry","Rohan","Hammad"]
normal = "i am normal argument :"
kw = {"Doctore":"Ravi","Police":"Vishal","Nurse":"Ankita"}
Function_argsss(normal,*har,**kw)