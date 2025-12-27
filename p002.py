n1=1
n2=2
s=0
while n1+n2<4*(10**6):
    n1,n2=n2,n1+n2
    if n2%2==0:s+=n2

print(s) 