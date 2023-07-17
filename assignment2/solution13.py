#solution13
#Write a Python program to sort a list of numbers in ascending order.
#input the list
def the_list():
    the__list = [] #initialise
    n = int(input("The no. of elements you want to add: "))
    for i in range(0, n):
        element = int(input("Enter a number: "))
        the__list.append(element)
    return the__list
#Let's sort
def sorting(lst):
    lst_sorted = sorted(lst) #using the sorted function
    return lst_sorted #generates a new list
#or
def sorting2(lst):
    lst.sort()  #using the sort method of the list object
    return lst #it changes the original list
#print the result
print(sorting(the_list()))
