# Starting off

# Program will calculate and print some numbers close to the value of pi as well as import math
print(22/7)
print(355/113)
import math

# Program will calculate and print some numbers even closer to the value of pi
print(9801/(2206 * math.sqrt(2)))

# Program will define archimedes
def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi

# Program will define average
def average(N):
    avg = 0
    for x in range(1, N + 1):
        avg = (avg + x)
    return avg/N

# Program w
def factorial(N):
    fact = 1
    for x in range(2, N + 1):
        fact = fact * x
    return fact

def fibonacci(N):
    acc0 = 1
    acc1 = 2
    for x in range(3, N+1):
        temp = acc1
        acc1 = acc0 + acc1  
        acc0 = temp
    return(acc1)

print(archimedes(8))
print(archimedes(16))

for sides in range(8, 999999, 8):
    print(sides, archimedes(sides))

# Q: experiment with the loop above alongside the actual value of Pi. How many sides does it take to make the two close?
# A: Pi is an irrational number, it has infinite many digits thus I am guessing infinitely many iterations

# Accumulators
# Commute the sum of the first 100 even numbers
acc = 0
for x in range(1, 101):
    acc = acc + x * 2
print(acc)
# Complete

# Commute the sum of the first 50 odd numbers
acc = 0
for x in range(0, 50):
    acc = acc + (x * 2 + 1)
print(acc)
# Complete

# Commute the average of the first 100 odd numbers
acc = 0
for x in range(0, 100):
    acc = acc + (x * 2 + 1)
acc = acc / 100
print(acc)
# Complete

# write a function that returns the average of the first N numbers, where N is a parameter
print(average(10))
# Complete

# Write a function called factorial that commutes the product of the first N numbers, where N is a parameter
print(factorial(5))
# Complete

# Each number in the Fibonacci sequence is the sum of the previous 2 numbers
# The first two numbers in the sequence are 1 and 1. Commute the 10th Fibonacci number
N = 10
acc0 = 1
acc1 = 2
for x in range(3, N+1):
  temp = acc1
  acc1 = acc0 + acc1  
  acc0 = temp
print(acc1)  
# Complete

# Write a function that commutes the Fibonacci number, where N is a parameter
# You may assume that N will be greater or equal to 3.
print(fibonacci(7))
# Complete

# A Monte Carlo simulation
import random
print(random.random())
# Complete

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
# Complete

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        t.goto(x,y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

showMontePi(1000)

# Your Task:
# Modify the simulation to plot points in the entire circle. You will have to adjustm the calculated value of pi accordingly.