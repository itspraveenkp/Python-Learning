
l = 50 
def function1(n):
    # l = 5
    global l
    l  = l + 20
    m = 8
    print(n, "i have printed")
    print(l,m)

function1("this is me")




def harry():
    x = 20 
    def Rohan():
        global x
        x = 10
        print("before calling Rohan",x)
        Rohan()
        print("After calling Rohan",x)
harry()






