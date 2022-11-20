a,b,l=map(int,input().split(" "))
l_final=l-1
if l == 1:print(a)
elif l>=2 and l%2==0:print((a+b)*(l//2))
elif l>2 and l%2==1:print(((a+b)*(l_final//2))+a)
