

# File handeling main methods are : Read , write and append 
# Read : 'r'  write = 'w' , append = 'a'


# Opening the file 

user_input = input("Enter the path of the file : ")

# If your file exist in the same folder you can just write the name of it 


# Reading the file 
file = open(user_input.strip('" "') , 'r')
# content = file.read()
# print(content)
# file.close()   # Best practice 


# Using readline( reading one line only)
# readline = file.readline()
# print(readline)
# file.close()

# Readlines ( read the lines in list form )

list_read = file.readlines()
print(list_read)
file.close()

# Writing the file

# write = file.write(" New thing added")
# print(write)
# file.close()