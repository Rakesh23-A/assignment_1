##   Palindrome

####  palindrome numbers from 1 to 1000

x=1
while x<=1000:
  p=x
  z=0
  while p>0:
    w=p%10
    p=int(p/10)
    z=z*10+w
  if z==x:
    print(x,end=' , ')
  x=x+1
