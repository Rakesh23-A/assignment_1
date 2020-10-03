### TRANSPORT

distance=float(input("enter the distance to be travel  [ in   KM ] : "))

weight=float(input("enter the weight of the goods   [ in   KG ] : "))

amount=0

if distance<=0:
    print("invalid information  [ please check ]")
else:
    if distance>=500:
        if weight<10:
            amount=7
        elif (weight>=10 and weight<100):
            amount=6
        else:
            amount=5
    
            
    else:
        if weight<100:
            amount=5
        else:
            amount=8


    print("\nAmount to be charged : ",distance*amount,' RS /--')
