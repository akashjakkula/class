num=int(input("enter the range "))
print("enter 2  starting numbers of fibonacci series")
a=int(input("a =  "))
b=int(input("b =  "))
print(a,b,end=" ")
for i in range(3,num+1):
    c=a+b
    a=b
    b=c
    print(b,end=" ")
