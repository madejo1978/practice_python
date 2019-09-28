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

def hotel_cost(nights):
  return nights * 140

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print (trip_cost("Los Angeles", 5, 600))

# Lists & Dictionaries
 # Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.


zoo_animals = ["pangolin", "cassowary", "sloth", "Brutus" ]

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])
    
# Index
 # You can access an individual item on the list by its index
 # The index appears directly after the list name, in between brackets

numbers = [5, 6, 7, 8]

print ("Print 5 + 7")
print (numbers[0] + numbers[2])
print ("6 + 8")
print (numbers[1] + numbers[3])

# List index can be used to access & to assign values (just like a variable).
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Change value "tiger" in the list
zoo_animals[3] = "hyena"
print (zoo_animals[3])

# List length
letters = ['a', 'b', 'c']
letters.append('d')
list_length = len(letters)
print ("There are %d items in the List letters." % (list_length))
print (len(letters))
print (letters)

# List slicing - general
letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3] # slices before 3 (not showing 3) 
print (letters)
print (slice)

# List slicing - string
animals = "catdogfrog"

 # The first three characters of animals
cat = animals[:3]
print (cat)

 # The fourth through sixth characters
dog = animals[3:6]
print(dog)

 # From the seventh character to the end
frog = animals[6:]
print(frog)

# List - maintaining order

 #search
animals2 = ["ant", "bat", "cat"]
print (animals2.index("bat"))

 #insert
animals2.insert(1, "insert before 1 bat")
print (animals2)

# List - For loop
 # if you want to do something with every item in the list
 # FOR variable IN list:

my_list = [1,9,3,8,5,7]
for for_loop in my_list:
  print (2 * for_loop)

# List - sort  
animals3 = ["cat", "ant", "bat"]
animals3.sort()

#for animals3 in animals3:
print (animals3)

# List - key / dictionaries
 # access values by looking up a key instead of an index (string or number)
 # login-pages, phonebooks
 # enclosed in curly braces (with key-value-pairs)
  # print is not with curly braces
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print (residents['Puffin']) 
print (residents['Sloth'])
print (residents['Burmese Python'])

# List / Dictionary - mutuable

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])

# Add 
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)

# del / rename
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

print ("There are " + str(len(zoo_animals)) + " animals in the zoo.")

 # del
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

# replace
zoo_animals['Rockhopper Penguin'] = 'Plains Penis'

print ("There are " + str(len(zoo_animals)) + " animals in the zoo.")

# remove function
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print (beatles)

# summary list/dictionary
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

 # Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

 # Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

 # Set the value of 'pocket' to be a list 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
 # sort
inventory['backpack'].sort()
 # remove
inventory['backpack'].remove('dagger')
 # add 55 to gold key
inventory['gold'] = inventory['gold'] + 50


# List - Function
 # using one element 
def list_function(x):
  return x[1] + 1

n = [3, 5, 7]
print (list_function(n))

# modify one element
def list_function2(x):
  x[1] = x[1] + 6
  return x

n = [3, 5, 7]
print (list_function2(n))

# List - manipulation 
 # add
my_list = [1, 2, 3]
my_list.append(4)
print (my_list)

# Print item by item
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print (x[i])
    
print_list(n)

# Multiply each element
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print (double_list(n))

# range()
 # shortcut function for generating a list
 # 3 versions: stop, start-stop, start-stop-step

# Iterating over a list 

 # method 1: FOR item in a list (not possible to modify)
list_for = [31, 11, 37]
for item in list_for:
  print (item)

 # method 2: iterate through indexes (uses indexes)
list_iterate = [31, 31, 31]
for i in range(len(list_iterate)):
  print (list_iterate[i])

# iterate strings 
n = ["Martin", "de", "Jonge"]

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print (join_strings(n))

 #  multiple lists 
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
  return x + y

print (join_lists(m, n))

# concatenates all sublists 
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print (flatten(n))

# LOOPS

# While-loop
 # similar to an if statement: it executes the code inside of it if some condition is true. The difference is that the while loop will continue to execute as long as the condition is true. 
 # in other words, instead of executing just onetime if true, it keeps executing while is true. 
 # inside a while loop, you can do anything you could do elsewhere, including arithmetic operations.

count = 6

if count < 5:
  print ("Hello, I am an if statement and the count is", count)
elif count > 5:
  print("Hello, I will not show an if statement because the count is > 5")
    

while count < 12:
  print ("Hello, I am an while statement and the count is", count) 
  count += 1

# Condition
 # expression that decides whether the loop is going to continue being executed or not.

loop_condition = True

while loop_condition:
  print ("I am a loop")
  loop_condition = False # if this expression is set to "True" it keeps on looping, i.c. printing

# The syntax for squaring a number is num ** 2
 # Print num squared <= 10
num = 1

while num <= 10:  
  num += 1
  print (num ** 2)

# While loop
 # often used for login-applications / to check if input is correct
 # for example to check if user input is valid

choice = input("Enjoying the course? (y/n)") # input()

while choice != 'y' and choice != 'n':  
  choice = input("Sorry, I didn't catch that. Enter again: ")

  