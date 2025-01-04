


# write the program to take user cost price and selling price to give profit and loss 



# Take input from user 
cost_price = int(input("Enter the cost price : "))
sell_price = int(input("Enter the selling price : "))

# Conditon for profit or loss
if cost_price > sell_price :
    print("You got loss ")
elif cost_price< sell_price :
    print("YOu have made a good profit ")
else :
    print("No profit no loss")    
