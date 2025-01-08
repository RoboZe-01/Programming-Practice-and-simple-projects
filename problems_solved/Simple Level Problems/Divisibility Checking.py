


# Python program to check if the number is divisible by 3 and 6 



# First check the input from the user 



# Doing error handeling and making it in a loop so it can e repeated till user gives currect answer 

while True :
    try :
        user_input = int(input("Enter the number you want to check : "))
        break
    except:
        print("Invalid format ")    


# Process 
while True:
    user_input = int(input("Enter a number: ")) 

    if user_input % 3 == 0 and user_input % 6 == 0:
        print(f'The Number {user_input} is divisible by both 3 and 6')
    elif user_input % 3 == 0:
        print(f"The number {user_input} is divisible by 3 only and not 6")
    elif user_input % 6 == 0:
        print(f'The number {user_input} only divisible by 6 and not 3')
    else:
        print(f" The number {user_input} is not divisible by 3 or 6")

    # Ask if the user wants to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break