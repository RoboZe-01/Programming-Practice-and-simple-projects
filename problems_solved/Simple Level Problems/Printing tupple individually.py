

# Write the python program to to print the the favourite colur in the tupple individually 

# SOlved with somple Method 

colour = ("Red","Pink","Black","skin","silver","White")

# a,b,c,d,e,f = colour

# print(a)
# print(b)                              # This method is simple but bit time consuming and sometimes confusing 
# print(c)
# print(d)
# print(e)
# print(f)


# Solved With method two ( Unpacking with * )

*colors,= colour         # * operator unpacks the tupple in the list which then can be printed

for col in colors :
 print(col)