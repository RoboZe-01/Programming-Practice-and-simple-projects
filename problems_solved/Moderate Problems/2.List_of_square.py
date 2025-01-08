

# Write a Python program to create a list of squares of all even numbers from 1 to 20 using list comprehension


# Steps to solve this problems is ,
# 1.create a loop which gives even numbers upto 20 
# 2.Store that in a variable
# 3.Square that and print it 

# Input (EVEN number upto 20 )
even = []
for i in range (1,21):
    if i %2 ==0 :
        even.append(i)

print(even)         

# Squaring the number 
square = [ val**2 for val in even]     # List comprehension
print(square)