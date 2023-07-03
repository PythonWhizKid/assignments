#Assignment 3
#Create an empty list
from time import sleep
print("Welcome to average calculator")
sleep(1)
list = []
n = int(input("Specify the number of elements you wish to calculate average for, press enter and start entering the numbers: "))
for i in range(0, n):
    #input numbers
    ele = int(input())
    #add the numbers to the list
    list.append(ele)
def average(x):  #define average function
    av = sum(x)/len(x)  #sum and len are predefined functions (sum gives the sum and len gives the lenghth of the list)
    return av  #return is the result of function
R = average(list)
sleep(1)
print("processing...")
sleep(0.8)
print("The average is ", round(R, 2))  #round is used to round off the variable to specified decimal places
