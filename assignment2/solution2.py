#solution 2
import math #for accurate value of pi
def area_circle(r):
    A = float(math.pi * r**2)
    print("The area of the circle is", round(A, 2))
radius = float(input("Enter radius of circle: "))
area_circle(radius)
