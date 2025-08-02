

# creating the function to give palindrome

# Palindrome : When the reverse of the string is same as normal

# Reusing the function created in the last problem

def reverse_str (x):          # Function defination
    return x[::-1]            # returning the reverse string

# a= "madam"  # using static varible 

# Let's  do this same using dynamic varible 

a = input("Enter the string to check Palindrome : ")

while True:
    a = input("Enter the string to check Palindrome : ")

    if a.lower() =="exit":
        print("Exiting the program, Have a good day")
        break

    if a == reverse_str(a):
        print(" This is palindrome")
    else:    
        print(" This is not the Palindrome")


