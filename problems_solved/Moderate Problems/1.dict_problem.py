


# Write Create a dictionary of student names and their corresponding roll numbers. 
# Write a function to search for a student's roll number given their name


# Make the dictonary Content sudent name and roll number 

student_dict = {13 : "Subha" , 7 :"Prem",15 :"Rahul",8 : "Om"}
while True :
            try :  
             user_input = int(input("ENter the roll number : "))
             break
            except :
             print("invalid roll no.")

def get_student_name() :
                name = student_dict.get(user_input)
                print(name)
get_student_name()