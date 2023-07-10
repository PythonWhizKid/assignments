#solution12
#Write a Python program to find the largest and smallest elements in a list.
def list_create(n):
    lst = []
    for i in range(0, n):
        input_ = input("Enter numbers: ")
        lst.append(input_)
    return lst
n = int(input("How many numbers do you want to include: "))
lst = list_create(n)
print(f"Largest number is {max(lst)} and smallest number is {min(lst)}")
        
