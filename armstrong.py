print("**ARMSTRONG NUMBER OR NOT**")
num=int(input("enter a number"))
temp=num
digits=0
s=0
while num:
    digits+=1
    num=num//10
num=temp
while num:
    rem=num%10
    s=s+rem**digits
    num=num//10
if temp==s:
    print(temp," is a armstrong number")
else:
        print(temp,"is not a armstrong number")
    
    
