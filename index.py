# print statements python 2 en python 3
print("Hello World")
print("Hello" + " Martin")
print("How do you make a hot dog stand?")
print("You take away its chair!")

# variables
todays_date = "17th September 2019"
product = 11 * 31
remainder = 1398 % 11

# updating variables
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

september_to_december_rainfail = 5.16 + 7.20 + 5.06 + 4.06
annual_rainfall += september_to_december_rainfail

# variables numbers
cucumbers = 3
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber

print (total_cost)

# two types of integers (Python 2!)
 # 1 method float() or 2 . after an integer    
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers/num_people
print (whole_cucumbers_per_person)

float_cucumbers_per_person = float(cucumbers)/num_people
print (float_cucumbers_per_person)

# multiline strings
haiku = """The old pond,
A frog jumps in:
Plop!"""

print (haiku)

# Booleans

# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

age_is_12 = False
name_is_maria = True

# value: string/integer/float?

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)

# assign variables (and print)

caesar = "Graham"
praline = "John"
viking = "Teresa"

print (caesar)
print (praline)
print (viking)

# Access variable by index

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print (fifth_letter)

# String methods
    # len() lower() upper() str()

parrot = "Norwegian Blue"
print (len(parrot))

parrot = "Norwegian Blue"
print (parrot.lower())

parrot = "norwegian blue"
print (parrot.upper())

pi = 3.14
print (str(pi))

# Methods that use dot notation only work with strings.

ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())

# Conversion to String to concatenate
  # print ("The value of pi is around " + 3.14)

print ("The value of pi is around " + str(3.14))

# String Formatting with %

string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))


#Library

from datetime import datetime
now = datetime.now()
print (now)

print(now.year)
print(now.month)
print(now.day)

# Formatting date with %
print ("%02d-%02d-%04d" % (now.day, now.month, now.year))
print ("%02d/%02d/%04d" % (now.day, now.month, now.year))

# Formatting time with %
print ("%02d:%02d:%02d" % (now.hour, now.minute, now.second))

# Formatting both on one line with %
print ("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))


# Boolean
 # comparators are: ==, !=, >, >=, <, and <=

# Make me true!
bool_one = 3 < 5  

# Make me false!
bool_two = 99 == "lettuce"

# Make me true!
bool_three = 44 / 2 <= 43

# Make me false!
bool_four = "potato" != "potato"

# Make me true!
bool_five = "tomato" == "tomato"

# Conditionals
 # Comparators
 # Boolean operators
 # Conditional statements

# boolean operators
 # three: not (1), and (2), or (3) (in this order)

 # if is a conditional statement 
  # executes after checking expression is True
  # use white space (before print-statement)
  # colons at the end

answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

# The else statement complements the if statement (if/else )
  # Unlike if, else doesn’t depend on an expression

# elif 
 # short for “else if.”

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))


def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
print (grade_converter(92))
print (grade_converter(70))
print (grade_converter(61))


# function
 # 3 components (header, comment, body)
 # call

def spam():
  """prints the string Eggs to the Console."""
  print ("Eggs") 

spam()

# Defining function 
 # placeholder variables are called parameters.
 # inputs into the function are called arguments.
 # call

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print ("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!

# Functions calling Functions
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

# example function with conditonal statements
def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False
  
# Generic import
 # import standard modules from Python, for example Math
 # => or: 
  # from module import function
   # just type sqrt() => no more math.sqrt()!
  

import math # get the sqrt() function from within math.  
print(math.sqrt(25))

from math import sqrt

# Universal import (from module import)
 # not adviseable creates a ton of unknown variables

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print (everything) # Prints 'em all!

# built-in functions:

# max()
maximum = max(-1,99,313131)
print (maximum)

# min()
minimum = min(-1,99,313131)
print (minimum)

#abs()
 #always returns a positive value
absolute = abs(-42)
print(absolute)

#  returns the type of the data it receives as an argument
print (type(108))
print (type(3.14))
print (type('hello'))

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"


from math import sqrt
value = sqrt(13689)
print(value)

def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"

def answer2():
  return 42
