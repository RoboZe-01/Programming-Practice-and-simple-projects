



# Write the program to reverse the integer and check if the reverse it same of different 





# to reverse the number we first convert this input integer to string 

def reverse_num():
    original = int(input("Enter the Number to reverse : "))
    original_str = str(original)
    reverse_str = original_str[::-1]
    reverse_int = int(reverse_str)
    print(f'The number {original} is reverse is {reverse_int}')


    # Condition to check if reverse is same as original 
    
    if reverse_int == original:
        print(f" reverse of {original} is same as {reverse_int}  ")
    else :
        print(" Reverse is not same ")    
reverse_num()

