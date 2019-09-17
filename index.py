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

# Value: string/integer/float?

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)