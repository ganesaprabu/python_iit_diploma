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
def my_function_args(*team):
  print("One of the team member is  " + team[1])
my_function_args("Jill", "Jam", "Sweety")
# If it is empty args, then it will throw error for out of index exception
#my_function_args() 


# Default value function
# If caller doesn't provide the value, default will work
def my_default_fun(city = "Chennai"):
  print("I am from " + city)
my_default_fun("Madurai")
my_default_fun()


# Passing the list to a function
def my_fun_getting_list(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_fun_getting_list(fruits)