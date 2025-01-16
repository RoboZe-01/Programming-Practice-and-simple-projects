



# Crete the python program to print the multiplication table using for loop


# Basic features : 1. User input 
                #  2. Error handeling 
                



# Take input from user
while True :            # usin while loop to ask until user privide valid number 
    try : 
        user_input = int(input("For which number you want multiplication table : "))
        print(f'Multiplication table for {user_input}')
        break
    except :            # handles invalid number 
        print("Enter the valid number !! ")    

for i in range (0,11):

    mul_table = user_input*i

    print(mul_table)       
    