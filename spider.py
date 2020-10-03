#Spider in Well
h=float(input("read a height : "))
u=float(input("read a jump : "))
s=float(input("read a slip : "))
if (s<0 or h<0 or u<0 or s>u):
  print("Invalid input ")
elif h==0:
  print("The Spider is out of well")
elif s==u:
  print("The Spider never reach top ")
else:
  i=(h-u)/(u-s)
  if (i%1)==0:
    i=i+1
  else:
    i=i+2
  print("The Spider out of well in  ",int(i),"  steps")
