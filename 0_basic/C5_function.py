# Simple
def my_function():
  print("Happy new year")

my_function();

# Parameterized
def my_function_year(year):
  print("Happy new year", year)
my_function_year(2022);

# More params
def my_function_welcome_msg(name, salutation):
  print("Hi ", salutation , name, ", Welcome to Python")
my_function_welcome_msg("John", "Mr.");

# Arbitrary Arguments, *args
def my_function(*team):
  print("One of the team member is  " + team[2])
my_function("Jill", "Jam", "Sweety")

def my_default_fun(city = "Chennai"):
  print("I am from " + city)
my_default_fun("Madurai")
my_default_fun()
