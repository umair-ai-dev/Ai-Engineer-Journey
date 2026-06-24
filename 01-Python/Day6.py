#WHILE LOOPS PROGRAM 

#Program-01

#Print numbers from 1-5
i = 1
while (i<=5):
    print(i)
    i +=1


#Program-02

#Print numbers from 1-100
i = 1
while i<=100 :
    print(i)
    i+=1

#Program-03

#Print numbers from 100-1
i = 100
while i>=1 :
    print(i)
    i-=1

#Program-04

#Print the multiplication table of a number'x'
n = int(input("Enter number:"))
i = 1
while  i<=10 :
    mul = n*1
    print(n, "*",i, "=", mul)
    i += 1

#Program-05

"""Print the element of the following list using a loop
    num = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]"""

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
print(len(num))
while i < len(num):
    print(num[i])
    i += 1
