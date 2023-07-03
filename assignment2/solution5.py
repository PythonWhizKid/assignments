def maximum():
    numbers = []
    for i in range(0,3):
        n = float(input("Enter numbers to find maxima: "))
        numbers.append(n)
    return print(float((max(numbers))))
maximum()
