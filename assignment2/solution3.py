#https://github.com/PythonWhizKid/assignments/blob/main/assignment1/solution4.py

#assignment 4
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backward. For example, "madam" and "racecar" are palindromic strings. 
from time import sleep
print("Palindrome check!")
sleep(1)
s = (input("Enter the word: "))
sleep(1)
#update
s = s.lower() #lowercase
s = s.replace(" ", "") #removed spaces
#/update
reverse_s = s[::-1]   #reversed the string by slicing
if reverse_s == s:
    print("The word is a Palindrome!")
else:
    print("Entered word is not a palindrome!")
    
#The above code works just fine for lowercase single words but to take it one step further and run the programme over any given string, we have to make some changes
#1 remove the spaces 
#2 lowercase all letters 
#3 and then reverse the string and check for palindrome
#added all this in the update portion above
        
