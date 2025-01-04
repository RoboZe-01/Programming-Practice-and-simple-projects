

# Writing the program to check wheter the entered number is even of odd




user_input = int(input("Enter the number you want to check : "))           # Taking inputs from user 

# Conditions to check it 

if user_input==0 :
     print("You entered 0 . ")  
elif user_input %2 ==0 :
    print("Entered number is even")
elif user_input %2 !=0:
    print("Entered value is odd")    
else:
    print("Please enter valid number ")    


 # Done Easy peasy    