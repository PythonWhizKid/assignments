#assignment 5
#The Fibonacci sequence starts with 0  and 1, and each subsequent number is the sum of the previous two numbers.
from time import sleep
#define a function that generates the sequence upto n
def seqgen(n):
    seq = [0, 1] #inititalizing the sequence
    while seq[-1] + seq[-2] <= n:  #checks wether the sum of previous two nummbers is less than, equal to n or not
        next_num = seq[-1] + seq [-2]
        seq.append(next_num)
    return seq
    
input = int(input("Enter the number: "))
print("Processing...")
sleep(1)
print(seqgen(input))
