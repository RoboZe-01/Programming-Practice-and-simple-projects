

# Count Words in a Sentence

# Return the number of words in a sentence (separated by spaces).

# Example: "Hello world" → 2

# Basic version : 

# user_input = input("Enter the sentence to know how many words are there : ")

# count = len(user_input.split())
# print(count)



# Advamced version : 

user_input = input("Enter the sentence to know how many words are there : ")

def count_words(sentence):

   if not  sentence.strip():     # Check if the input is empty
      print("Empty string")
   words = sentence.split()   # converts the words to string inside the lists
   
 
   return len(words)          # returns the len of the list 
 
print(f"Your sentence have this much of words : {count_words(user_input)}")