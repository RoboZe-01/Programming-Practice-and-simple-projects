


# Project Done by RoboZe ( Prem )

# This Project is the Part of making 5 unique project in 2 days     
# To end the year with the feeling of accomplishment


         ### WhatsApp Automation ### 

# Main features are : 
#         1.user can give input number , date , time 
#         2. Only valid input will be accepted 
#         3. simple and clear instructions 
#         4.Time to send the message will be easily shown 


  # Important Documentation for more information :
    #  For pywhatkit : https://www.geeksforgeeks.org/introduction-to-pywhatkit-module/
    #  for datetime  : https://www.geeksforgeeks.org/python-datetime-module/
#   ( Copy the link and learn more )

# Importing pywhatkit and datetime 

# use  ( python -m pip install pywhatkit ) to install it 


import pywhatkit as kit
from datetime import datetime

# Function to validate phone number
def is_valid_phone_number(phone):
    return phone.startswith("+") and phone[1:].isdigit() and len(phone) >= 10

# Function to validate time
def is_valid_time(hour, minute):
    return 0 <= hour <= 23 and 0 <= minute <= 59

# Function to validate date
def is_valid_date(year, month, day):
    try:
        datetime(year, month, day)  # Attempt to create a datetime object
        return True
    except ValueError:
        return False

# Schedule a WhatsApp message
def schedule_message():
    # Input recipient's phone number
    while True:
        phone_number = input("Enter recipient's phone number (with country code, e.g., +91XXXXXXXXXX): ").strip()
        if is_valid_phone_number(phone_number):
            break
        print("Invalid phone number! Ensure it starts with '+' and contains digits.")

    # Input the message
    message = input("Enter the message to send: ")

    # Input the date for scheduling
    while True:
        try:
            date_input = input("Enter the date to send the message (YYYY-MM-DD): ")
            year, month, day = map(int, date_input.split("-"))
            if is_valid_date(year, month, day):
                break
            print("Invalid date! Ensure it is in the format YYYY-MM-DD.")
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    # Input the time for scheduling
    while True:
        try:
            time_input = input("Enter the time to send the message (HH:MM, 24-hour format): ")
            hour, minute = map(int, time_input.split(":"))
            if is_valid_time(hour, minute):
                break
            print("Invalid time! Ensure hour is between 0-23 and minute is between 0-59.")
        except ValueError:
            print("Please enter a valid time in HH:MM format.")

    # Combine date and time
    schedule_datetime = datetime(year, month, day, hour, minute)
    current_datetime = datetime.now()

    if schedule_datetime <= current_datetime:
        print("The scheduled date and time must be in the future!")
        return

    # Send the message using pywhatkit
    try:
        print(f"Scheduling your message to {phone_number}...")
        kit.sendwhatmsg(phone_number, message, hour, minute, wait_time=20)  # 20 seconds to prepare
        print(f"Message scheduled successfully for {schedule_datetime.strftime('%Y-%m-%d %H:%M')}!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    print("Welcome to WhatsApp Message Automation!")
    schedule_message() 

