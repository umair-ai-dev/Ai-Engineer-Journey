# #LISTS PROGRAMS

#Program for store movies name in list
movie=[]

mov1= input("enter first movie:")
mov2= input("enter second movie:")
mov3= input("enter third movie:")

movie.append(mov1)       #  |
movie.append(mov2)       #  } this is used to add movie name inside list
movie.append(mov3)       #  |
print(movie)


#same Program from 2nd method
movie=[]

mov=input("enter first movie:")
movie.append(mov)
mov=input("enter second movie:")
movie.append(mov)
mov=input("enter third movie:")
movie.append(mov)

print(movie)


#same Program from 3rd method
movie=[]

movie.append(input("enter first movie:"))
movie.append(input("enter second movie:"))
movie.append(input("enter third movie:"))

print(movie)


#Program to check if a list contain Palindrome element
list=list(input("enter elements separated by space:"))

copy_list=list.copy() #  Making copy of list
copy_list.reverse()  # Reverse the copy    

if(copy_list==list):     
    print("PALINDROME")  #if equal then it's Palindrome
else:
    print("NOT PALINDROME")  #if not equal then it's not Palindrome


#TUPLES PROGRAMS

#Program for count the number of student with "A" grade 
grade=tuple(input("enter grade separated by space:").split())
ch= input("enter grades to count:")
print(input(grade.count(ch)))


#Program for printing input into ascending order 
grades=tuple(input("enter grade:").split())
sorted_grades = tuple(sorted(grades))
print(sorted_grades)
