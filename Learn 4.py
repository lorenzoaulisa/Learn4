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

# Commute the sum of the first 100 even numbers
acc = 0
for x in range(1, 101):
    acc = acc + x * 2

print(acc)

# Commute the sum of the first 50 odd numbers
acc = 50
for x in range(1, 50):
    acc = acc + x * 2

print(acc)

# Commute the average of the first 100 odd numbers
acc = 0
for x in range(1, 200):
    if x % 2 :
        acc = (acc + x)

print(acc/100)

acc = 0
for x in range(1, 50):
    acc = (acc + x)

# Commute the sum of the first 100 even numbers
# Complete

# Commute the sum of the first 50 odd numbers
# Complete

# Commute the average of the first 100 odd numbers
# Complete

# write a function that returns the average of the first N numbers, where N is a parameter
# In progress

# Write a function called factorial that commutes the product of the first N numbers, where N is a parameter


# Each number in the Fibonacci sequence is the sum of the previous 2 numbers


# The first two numbers in the sequence are 1 and 1. Commute the 10th Fibonacci number

# Write a function that commutes the Fibonacci number, where N is a parameter

# You may assume that N will be greater or equal to 3.



# A Monte Carlo simulation

import random

print(random.random())

# Boolean expressions
# >  greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == the same as [ equal to ]
# != NOT equal to

CatWeight = 15
print(CatWeight > 15)
print(CatWeight >= 15)
print(CatWeight <= 15)
print(CatWeight < 15)
print(CatWeight == 15)
print(CatWeight != 15)

BigLion = 40

# compound boolean operations
# and
# or
# not

print(CatWeight < 30 and BigLion < 55)
print(CatWeight < 30 or BigLion < 55)
print(not BigLion < 9999)

# Decision Making -- Selection statements
a = 5
b = 10
c = 75

if a > b :
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:
    c = 1050
    if b == a:
        c = 25


print(a, b, c)


d = 55
e = 72
f = 44
ans = 0

if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)