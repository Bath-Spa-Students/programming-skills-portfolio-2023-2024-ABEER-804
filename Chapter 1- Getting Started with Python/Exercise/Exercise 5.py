#Exercise 5 'Write a phyton program which accepts the radius of a circle from the user and compute the area.'
import math
radius = float(input("Enter the radius of circle:"))
area = math.pi * radius * radius
print ("area of the circle is {0}".format(area))