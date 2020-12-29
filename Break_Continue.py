i = 0
while(True):
    if i +1 < 5:
        i = i + 1
        continue
    print(i +1, end= " ")

    if(i == 44):
        break
    i = i + 1
        
i = 0
while(True):
    inp = int(input("\n Enter Your Number :"))
    if inp > 100:
        print("Congrates you have entered number grater than 100")
        break
    else:
        print("Try again")
        continue


