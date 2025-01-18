

# Write the program to create a new text file and write the list of names in it . 


user_input = input("Enter the path of the file: ")

# Handle potential issues with user input
try:
    with open(user_input, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: File '{user_input}' not found.")
except PermissionError:
    print(f"Error: You don't have permission to access '{user_input}'.")
except Exception as e:  # Catch other unexpected errors
    print(f"An unexpected error occurred: {e}")