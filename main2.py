#import necessary modules
from collections import Counter #Used for word frequency
from textstat import textstat #Already installed. You may need to install if not working.

#Analyze the file for word frequency and total word count
def frequency_analysis(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read().lower() #Convert to lowercase for ease of handling.
            words = text.split() #Split the text into words.
            word_count = len(words)
            print(f"The total word count for your text sample is {word_count}.")
            word_frequency = Counter(words)
            print(f"The word frequency is {word_frequency}.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#Analyze the file for readability score
def readability_score(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            readability_score = textstat.flesch_reading_ease(text)
            print("This program asseses readability using 'Flesch Reading Ease.' Higher scores indicate easier readability.")
            print(f"The readability score for your text sample is {readability_score}.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#greet the user
name = input("Hello user. What is your name? ")
 
#Give overview on the program's function and take user input on how to proceed.
print(f"{name}, I can help you analyze a text sample. Please let me know if you want to check for total word count and word frequency, or provide you a readability score.")
choice = input("Please enter your choice. Enter 1. for word frequency or 2.for readability score. ")

#Handle/validate text input. If inputs are valid, strip the formatting from the input to allow for variation in input formats and ease of handling.
if choice == "1" or choice == "1.": 
    choice = "1"
    print("You have chosen to check for word frequency.")
elif choice == "2" or choice == "2.":
    choice = "2"
    print("You have chosen to check for readability score.")
else:
    print("Invalid choice. Please enter 1 or 2. ")
    exit()

#Prompt for further input. 
file_name = input("What is your file name and the location? ")
if file_name == "":
   print("Invalid file name. Please enter a valid file name. ")
else:
    print(f"Thank you, {name}. File name is valid.")

if choice == "1":
    frequency_analysis(file_name)
else:
    readability_score(file_name)



 

 

