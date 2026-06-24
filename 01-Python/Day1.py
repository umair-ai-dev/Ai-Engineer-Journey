#Program-01

# first program 
print("hello world!")

#Program-02

# name and about
name= input("enter your name:")
print(f"Hello my name is {name},this is my Ai journey.")

#Program-03

# Data types
a=10
b=2.0
c= "umair"
d= True
print(type(a))
print(type(b))
print(type(c))
print(type(d))



#Program-04

# program for adding two numbers
a= int(input("enter first number:"))
b= int(input("enter second number:"))
print("sum =", a+b)


#Program-05

# program for Normal Calculation
a= int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))
sum = a+b
diff = a-b
mul = a*b
divide = a/b
rem = a%b
print(sum)     #for addition
print(diff)     #for Substraction
print(mul)     #for multiplication
print(divide)  #for division
print(rem)     #for reminder


#Program-06

# program for age checker
x=int(input("enter your age:"))
if(x>=18):
    print("adult")
else:
    print("not adult")


#Program-07

# program for license or vote 
x= int(input("enter age:"))
if(x>=18):
    print("can drive and can vote:")
else:
    print("can't derive and can't vote")


#Program-08

# program for print area
side= float(input("enter square side:"))  #taking input of a square side 
print("area=", side*side)


#Program-09

# program for finding average
a= float(input("enter first number:"))
b= float(input("enter second number:"))
print("avg =", (a+b)/2)


#Program-10

# program for find True or False
a= int(input("enter first num:"))
b= int(input("enter second num:"))
print(a>=b)
