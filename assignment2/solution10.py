#solution10
#Write a program to find the sum of digits of a number
#create a function
def list_digits(n):
    char = list(n) #breaks string into characters
    return char
def sum_digits(lst):
    addition = 0
    for i in lst:
        addition = addition + int(i)  #converting characters into integers here is an important part... I missed it earlier
    return addition
number = input("Enter a number: ")
list_digits = list_digits(number)
result = sum_digits(list_digits)
print(f"Sum of digits of {number} is {result}")
    
