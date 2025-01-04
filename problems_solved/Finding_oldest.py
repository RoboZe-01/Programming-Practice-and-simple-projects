


# Three Ages will be given as a input for the function we have to find out the oldest among threee 

a = int(input(" Enter the first Age : "))
b = int(input("ENter the second age : "))
c = int(input("Enter the third age : "))

def oldest():
    if a > b and a>c:
        print(f'First age {a} is oldest ')
    elif b >a and b>c :
        print(f'Second age {b} is oldest ')    
    else :
        print("Third age {c } is oldest ")    
        
oldest()