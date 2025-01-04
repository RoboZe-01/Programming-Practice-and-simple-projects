

# Write the python to take three angle input and check whether it can make triangle or not 


# COndition for triangle : Sum of all sides is 180 



# Take inputs 
first_angle = int(input("Enter the first angle : "))
second_angle = int(input(" Enter the second angle "))
third_angle = int(input("Enter the third angle : "))

# Make new variable which includes summation of all angles 
sum_angles = first_angle + second_angle + third_angle

#Condition to check triangle or not 

if sum_angles == 180 :
    print("This will make triangle ")
else : 
    print(" Will not form triangle ")    