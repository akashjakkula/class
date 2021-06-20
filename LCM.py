print("enter 2 numbers for LCM")
num1=int(input("enter a number"))
num2=int(input("enter another number"))
if num1>num2:
    num1,num2=num2,num1
i=num2
while True:
    if i%num1==0 and i%num2==0:
        print("{} , {} is LCM of  {} ".format(num1,num2,i))
        break
    i+=1
    

