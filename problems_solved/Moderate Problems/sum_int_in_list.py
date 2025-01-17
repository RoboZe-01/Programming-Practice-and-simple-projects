

# Write the python program to give sum of all the numbers in the list , but stop when sum exceeds 100 


# In this problem there are some things to considerr before diving into the actual code that is
# First how user  enter the input
# how to validate that input and convert that to list
# Rest is easy 
 



input = input("Enter the numbers with sapce to seperate them : ")
list_input = input.split(" ")

summation = 0
for i in list_input() :

    summation+= i 
print(summation)    
