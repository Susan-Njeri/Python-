# age=25
# if age>=25:
#     print("You are an adult")
#     print("You can vote")
# else:
#     print("You are a minor")
#     print("You cannot vote")
#     years_to_wait = 25-age
#     print(f"Wait{years_to_wait} more years")
    
    #Multiple conditions with elif
    #syntax
    # if condition1:
    #   code to execute if condition1 is true
    # elif condition2
    #  code to execute if condition1 is false and condition2 is true
    # elif condition3
    #  code to execute if condition1 and condition2 are false and condition3 is true
    # else
    #  code to execute if all the conditions are false
    
score=85
    
if score>=90:
        print("Excellent Performance")
elif score>=80:
        grade='B'
        print("Good Job")
elif score>=70:
        grade='C'
        print("You Passed")
else:
        grade='F'
        print("You need to study more")
        print(f"Your grade is {grade}")
        
# Loops
# allow us to
# for loops
# the 'for' loop is used when you know how many timesyou want to repeat something let' explore different ways to use it
# range data type
# helps you construct your own range of numbers
# a list of integers from 0-9 [0,1,2,3,4,5,6,7,8,9]
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# using the range function to construct the list
print(list(range(11))) #11 wont be included [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(5, 10))) # 10 wont be included [5, 6, 7, 8, 9]
print(list(range(0, 11, 2))) # step of 2, skips the second number [0, 2, 4, 6, 8, 10]

# Back to loops

# for loop syntax
# for temp_variable in sequence/iterable:
#  code goes here...

print("Counting from 0 to 4")
for number in range(5):
    print(f"Current number: {number}")
    
print("\nCounting from 1 to 5")#0,1,2,3,4
for number in range (1,6):
    print(f"Current number: {number}") #1,2,3,4,5
    
# Print even numbers 0 to 10
# range with step
print("\nEven numbers from 0 to 10")
for number in range (0,11,2):
    print(f"Even number: {number}")

# Looping through a string
name='Python'
print("\nLetters in Python")
for letter in name:
    print(letter)
    
# looping with enumerate to get index and value
colors=['red','green','blue']
print('\nColors with their indices')
#for index, color in enumerate(colors):
for index, color in enumerate(colors, start=1):
   print(f"Color{index}: {color}")
    #print(f"Color{index+1}: {color}")

# mathematical times table using a loop
for x in range(1,13):
    print(f"{5} x {x}={5*x}")
    print(f"{7} x {x}={7*x}")

# While Loop
# syntax
# while condition
#   code to execute

# basic while loop
count=0
while count <5:
    print(f"Count is: {count}")
    count += 1 #same as count = count +1
