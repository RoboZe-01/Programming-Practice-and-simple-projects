
# Problem Statement : 
#   Remove Whitespace
#    Remove all leading/trailing spaces from a string.

#  Example: " hello " → "hello"


def rmv_wht_space(input):

    return input.strip()             # So we use strip method to remoce the white spaces from the string 

# var = input("Enter the strings to remove white spaces : ")
var = "  hi  "
print(rmv_wht_space(var))
