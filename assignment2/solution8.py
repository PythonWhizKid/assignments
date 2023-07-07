#solution8
from time import sleep
#First lets create a function to count occurences of a specific element
def count_occurences(array, element):
    count = 0 #initialise the count at 0
    for i in array:
        if i == element:
            count += 1 
    return count
#Now we can make lists
ourlist = ["happy", "sad", "happy", 1, "sad", 1, 1, 56, "elephant", "birthday", 56]
print("List: ",ourlist)
sleep(0.8)
input1 = input("Enter 'add' if you want to add more items to the list or 'c', if you want to continue... ")
sleep(0.8)

if input1 == "add": #allow user to add items to list
    n = int(input("How many elements do you want to add? "))
    for i in range(0, n):
        
        element_add = str(input("Enter the element: "))
        ourlist.append(element_add)
    sleep(0.8)    
#implement the function
element_tar = input("Enter the target element to count occurences: ")
sleep(0.8)
print("Number of occurences of %s is %d" % (element_tar, count_occurences(ourlist, element_tar)))
        
            
