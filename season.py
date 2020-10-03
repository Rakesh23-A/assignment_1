###  SEASON

print("Format should be  :-  January  ")

M=input("Enter the Month  : ")

A={"Winter":["December","January","February"],"Spring":["March","April","May"],"Summer":["June","July","August"],"Autumn":["September","October","November"]}

for i in A:
    if M in A[i]:
        print(M," is in : ",i,)
