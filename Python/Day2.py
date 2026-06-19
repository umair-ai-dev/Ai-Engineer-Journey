#STRINGS PROGRAMS 

#program for printing length of a text 
name = input("enter your name:")
print("length of name =",len(name))

#program find occurrence in string
str = "Hi there , $iam going buy a car in $ for just $99.9" 
print(str.count("$"))  #output will be 3


#CONDITIONS PROGRAMS 

#Assigning grades using conditional loop
marks= int(input("enter marks:")) #taking wanted marks from user
if(marks>=(33)):
    print("passed")
else:
    print("failed")


#program for check even or odd
num= int(input("enter number:"))
rem= num%2
if(rem==0):
    print("even")
else:
    print("odd")


#program for assigning grades
marks= int(input("enter numbers:"))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="D"
print(f"grade of student={grade}")


#program to find greater of three
a= int(input("enter first number:"))
b= int(input("enter second number:"))
c= int(input("enter third number:"))

if(a>=b and a>=c):
    print(f"largest is a = {a}")
elif(b>=a and b>=c):
    print(f"largest is b = {b}")
else:
    print(f"largest is c = {c}")


#program for check number is a multiple of seven 
x= int(input("enter number:"))

if(x%7==0):
    print("MULTIPLE")
else:
    print("NOT A MULTIPLE")
