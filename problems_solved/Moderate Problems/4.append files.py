

# Write the python program to append new lines in existing file

User_input = input("Enter the path of the file : ")

file = open (User_input.strip('" "' ),'+a')
file.write("Hii ")
print(file)
file.close()
