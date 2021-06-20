num=int(input("enter a number"))
rev=0
while num:
    rem=num%10
    rev=rev*10+rem
    num=num//10

print("the reverse number is {}".format(rev))
