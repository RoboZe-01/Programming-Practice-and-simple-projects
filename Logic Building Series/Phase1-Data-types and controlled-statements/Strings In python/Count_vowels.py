  # Problem statement : 
# Count Vowels

# Count the number of vowels (a, e, i, o, u) in a string.

# Example: "apple" → 2

# Making a global varible for vowels

vowels = ('a','e','i','o','u','A','E','I','O','U')

while True :                                                     # Loop to make the programmew work till user exit the programme
    var = input("Enter to count the wels (to exit press Y) : ")
    if var.lower()=="y":                                        # Condition to exit the programme
        print("Exiting the programme, Have a good day !")          
        break

    count = 0                                                   # Variable to store the count of the vowel
    for i in var.lower():
        if i in vowels :
            count+=1
    print(f"Number of vowels are : {count}")        



