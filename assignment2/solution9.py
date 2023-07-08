#solution9
#Write a Python program to check if a given string is an anagram
def list_maker(string):
    lowercase = string.lower()
    space_remove = lowercase.replace(" ","")
    lst = list(space_remove)
    return lst
def anagram_check(lst1, lst2):
    if len(lst1) != len(lst2):
        print("These strings are not anagrams")
        return False
    else:
        sorted1 = sorted(lst1) #use sorted function to sort lists
        sorted2 = sorted(lst2)
        if sorted1 == sorted2:
            print("These strings are anagrams")
            return True
        else:
            print("These strings are not anagrams")
            return False
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
lst1 = list_maker(string1)
lst2 = list_maker(string2)
anagram_check(lst1, lst2)

            
