


# User will input (2numbers).Write a program to swap the numbers

# There are different ways to do this problem 


# First method : Using simple built in method 
# that is ,   : x,y = y,x






a = int(input(" Enter the first number  : "))
b = int(input(" Enter the second number : "))

print (f' before swapping')
print(f' X is : {a} and Y is: {b}')

a,b = b,a 


print("After Swapping : ")
print( f'X becomes : {a} and Y becomes {b}')
