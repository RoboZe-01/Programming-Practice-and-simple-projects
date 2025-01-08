

#Python program to find simple interest when principle , rate of interest and time period is given 


# For this what will be 
       # Input : 1.Principle ( Amount of money borrowed )
                #  2. Rate of interest 
                #. Time period 

# Process : In this we directly have a formula for this , so main objective will be to take input and make a 
# Function to add input to the formula 

# Output : Simple interest value 



# Taking inout from the user 
p= int(input("Enter the amount of money borrowed : "))          # Principle 
r = int(input("Enter the rate of interest : "))                # Rate of interest 
t = int(input("Enter the time period you want money for : "))  # Time period ( In Months )


# Process : Make the function to calculate Simple interest by taking the inputs 

def simple_interest():

    sim_interest = (p*r*t)/100

    # Output 
    print(sim_interest)
    return sim_interest


simple_interest()







