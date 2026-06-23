#first program 
print("hello world!")

#name and about
name= input("enter your name:")
print(f"Hello my name is {name},this is my Ai journey.")

#Data types
a=10
b=2.0
c= "umair"
d= True
print(type(a))
print(type(b))
print(type(c))
print(type(d))



#program for adding two numbers
a= int(input("enter first number:"))
b= int(input("enter second number:"))
print("sum =", a+b)


#program for Normal Calculation
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


#program for age checker
x=int(input("enter your age:"))
if(x>=18):
    print("adult")
else:
    print("not adult")


#program for license or vote 
x= int(input("enter age:"))
if(x>=18):
    print("can drive and can vote:")
else:
    print("can't derive and can't vote")


#program for print area
side= float(input("enter square side:"))  #taking input of a square side 
print("area=", side*side)


#program for finding average
a= float(input("enter first number:"))
b= float(input("enter second number:"))
print("avg =", (a+b)/2)


##program for find True or False
a= int(input("enter first num:"))
b= int(input("enter second num:"))
print(a>=b)


