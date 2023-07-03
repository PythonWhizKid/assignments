#solution1
def prime_check(n):
    if n < 2:
        print("The given number is not a prime number")
        return
    for i in range(2, int(n**0.5)+1): #factors bigger than square root will eventually be multiplied b factors smaller than it as 36 = 12*3
        if n % i == 0:
            print("The given number is not a prime number")
            return
    print("The given number is a prime number")
        
input = int(input("Enter a number: "))
prime_check(input)
