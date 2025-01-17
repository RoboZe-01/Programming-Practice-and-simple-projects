


# Write the python program to read the text from files and write that down to the console 



# user input 
user_input = input("Enter the path of the file : ")  # just 


with open(user_input.strip('" "'),'r') as file :            # So here Strip() function is main and used to remove double quotes from the input 
    content = file.read()
    print(content)

