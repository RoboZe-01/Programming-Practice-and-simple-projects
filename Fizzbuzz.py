Language used : Python 

# Fizz Buzz Problem  : In this Print number from 1 to 100 however when the number will be divisible by 3
# print fizz and when number is divisible 5 print buzz



for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if not output:
        output = str(i)
    print(output)

      

        
   


