# Starting off

print(22/7)
print(355/113)
import math

print(9801/(2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range(8, 999999, 8):
    print(sides, archimedes(sides))

# Q: experiment with the loop above alongside the actual value of Pi. How many sides does it take to make the two close?
# A: I'm guessing infinitely many

# Accumulators
acc = 0
for x in range(1, 101):
    acc = acc + x * 2

print(acc)

acc = 0
for x in range(1, 51):
    acc = acc + x * 2

print(acc)

# Commute the sum of the first 100 even numbers
# Commute the sum of the first 50 odd numbers
# Commute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where N is a parameter
# Write a function called factorial that commutes the product of the first N numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous 2 numbers
# The first two numbers in the sequence are 1 and 1. Commute the 10th Fibonacci number
# You may assume that N will be greater or equal to 3.
