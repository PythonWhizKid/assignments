#solution11
#Write a Python program to generate the Fibonacci sequence
def fib_seq(n):
    seq = [1,2] #initialise the seq (important or seq[-1] and seq[-2] won't work)
    while seq[-1] + seq[-2] <= n:
        next_ = seq[-1] + seq[-2]
        seq.append(next_)
    return seq
n = int(input("Enter the number to print Fibonacci sequence upto: "))
print(fib_seq(n))
