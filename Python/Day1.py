#first program 
print("hello world!")

#name and about
name= input("enter your name:")
print(f"Hello my name is {name},this is my Ai journey.")

#data types
a=10
b=2.0
print(float(a))
print(int(b))

#Normal Calculator
a= int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))
sum = a+b
sub = a-b
mul = a*b
divide = a/b
rem = a%b
print(sum)     #for addition
print(sub)     #for minus
print(mul)     #for multiplication
print(divide)  #for division
print(rem)     #for reminder


#age checker
x=int(input("enter your age:"))
if(x>=18):
    print("adult")
else:
    print("not adult")


#license or vote 
x= int(input("enter age:"))
if(x>=18):
    print("can drive and can vote:")
else:
    print("can't derive and can't vote")


