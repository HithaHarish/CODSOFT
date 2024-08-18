def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def floatdiv(a,b):
    return a/b
def intdiv(a,b):
    return a//b
def moddiv(a,b):
    return a%b
def exp(a,b):
    return a**b
print("MATHMATE - THE BASIC VERSION OF A CALCULATOR")
print("Welcome to the MATHMATE!")
try:
    print("Kindly enter the 2 numbers.")
    no1=float(input("Enter the Number 1:"))
    no2=float(input("Enter the Number 2:"))
except:
    print("Enter any 2 integers or floating points only")
    no1=float(input("Enter the Number 1:"))
    no2=float(input("Enter the Number 2:"))
print("The following operations are available on Mathmate")
# Here, op stands for operation
ops=["ADDITION","SUBTRACTION","MULTIPLICATION","FLOATING DIVISION","INTEGER DIVISION","MODULO DIVISION","EXPONENTATION"]
opkeys=["A","S","M","FD","ID","MD","E"]
for i in range(7):
    print("To Perform %s,ENTER the key %s"%(ops[i],opkeys[i]))
op=(input("Enter the key:")).upper()
if op=="A":
    RESULT=add(no1,no2)
elif op=="S":
    RESULT=sub(no1,no2)
elif op=="M":
    RESULT=mult(no1,no2)
elif op=="FD":
    RESULT=floatdiv(no1,no2)
elif op=="ID":
    RESULT=intdiv(no1,no2)
elif op=="MD":
    RESULT=moddiv(no1,no2)
elif op=="E":
    RESULT=exp(no1,no2)
ind=opkeys.index(op)
print(ops[ind], "of",no1,"and",no2,"results in",RESULT)

