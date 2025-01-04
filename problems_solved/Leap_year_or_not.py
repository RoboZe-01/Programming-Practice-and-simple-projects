


# Write a python program to check whether the give year is leap year or not 




# Using normal method 

input_year = int(input("Enter the year u want to check : "))

if input_year % 4==0:
    print(f"Entered year {input_year} is leap year ")
else :
    print("This is normal year !! No extra day ")    



# Using inbuild function isleap()          

import calendar
year = int(input("Enter the year to check : "))
check = calendar.isleap(year)

print(check)