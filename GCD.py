print("enter 2 numbers for GCD")
num1=int(input("enter a number"))
num2=int(input("enter another number"))
if num1>num2:
    num1,num2=num2,num1
i=num1
while True:
    if num1%i==0 and num2%i==0:
        print('{} ,{} is GCD of {}'.format(num1,num2,i))
        break
    i-=1
        
    
