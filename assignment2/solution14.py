#solution14
def list_gen():
    lst1 = []
    lst2 = []
    n = int(input("How many elements do you want in list 1: "))
    for i in range(0, n):
        element = input("Enter an element: ")
        lst1.append(element)
    n2 = int(input("How many elements do you want in list 2: "))
    for i in range(0, n2):
        element2 = input("Enter an element: ")
        lst2.append(element2)
    return lst1, lst2
def common(lst1, lst2):
    common_elem = []
    for elem in lst1:
        if elem in lst2:
            common_elem.append(elem)
    result = set(common_elem)    #removes repeatations of all elements (represent the list as set)
    return result
lst1, lst2 = list_gen()
print(f"The common elements are {common(lst1, lst2)}")
