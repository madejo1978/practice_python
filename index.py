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