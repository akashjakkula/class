def add(a,b):
    return(a+b)

def sub(a,b):
     return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a//b)

a=int(input("a =  "))
b=int(input("b =  "))
c=add(a,b)
print("addition=",c)
c=sub(a,b)
print("subtraction=",c)
c=mul(a,b)
print("multiplication=",c)
c=div(a,b)
print("division=",c)
