num=int(input("enter a number"))
rev=0
rem=0
temp=num
while num:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("{} is reverse of {} ".format(temp,rev))
if temp==rev:
    print("the given number is palindrom number")
else:
    print("the given number is not a palindrome")

