# Boolean type

flag = True
print('In True, "T" should be caps ->', flag)

result = False
print('In False, "F" should be caps', result)
print()

# Only 0 or 0.0 in integer and floating are False
# all other positive or NEGATIVE values will be true

flag = bool(123)
print('Positive values are True ->', flag)
flag = bool(0)
print('Zero are False ->', flag)
flag = bool(-123)
print('NEGATIVE values are True ->', flag)
print()

# Empty strings are False
# Non-Empty strings are True
flag = bool('USA')
print('Non empty values are True ->', flag)
flag = bool('')
print('empty values are False ->', flag)

print()



print()