value = '0123456789'

a = value[2]
b = value[3]
print('No type conversion happened, it will be string concatenation-> ', a+b)
print()

# Explicit type conversion happened
a = int(value[2])
b = int(value[3])
print('No type conversion happened, it will be string concatenation-> ', a+b)
print()

# Slicing of Str
slicedValue = value[2:5]
print('sliced Value', slicedValue)