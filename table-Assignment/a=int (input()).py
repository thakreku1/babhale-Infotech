a=int (input())
b=int(input())
z=0
l=[]
if a>b:
  z=z+b
else:
  z=z+a
for i in range (2, z+1):
  if a%i==0 and b%i==0 :
    l.append(i)
print(max(l))       