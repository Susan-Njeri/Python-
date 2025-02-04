# Booleans (bool)- True or False values
# the first character is always capitalized

is_raining= True
has_coffee= False
# Boolean operations
# not-denies an expression
print(not is_raining) #False

# and (both operands must be true, to have a true result)
# eg.email logins
print(is_raining and has_coffee) #False

# or - atleast one operand is true it will be true
print(is_raining or has_coffee) #True

# Comparison Operators- used to compare two or more values (create booleans)
x=5
y=10

# less than (<)
print (x<y) #True

# greater than (>)
print(x>y) #False

# equal to (==)
print(x==y) #False

# Not equal to (!=)
print(x!=y) #True

# less than or equal to (<=)
print(x<=y) #True

# greater than or equal to (>=)
print(x>=y) #False

# Common boolean patterns
age=20
has_license= True
# create a variable to check if the person is an adult
is_adult= age>=18
print(is_adult) #True

# create a variable to check if the person can drive
can_drive=(age >= 16) and has_license
print(can_drive) #True

# Next class -> Control Flow in Python
# control-flow.py
