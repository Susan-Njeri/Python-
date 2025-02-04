# Built in function
# absolute value
# print(abs(-5)) #5

# #round 3.14159 to 2 decimal places
# print(round(3.14159,2))

# # maximum value-max()
# print(max(1,2,3)) #3

# # minimum value-min()
# print(min(1,2,3)) #1

# #data type conversion
# price="19.99"
# quantity="5"

# #convert the price to float 'float()' and quantity to integer 'int()'
# total_price=price * 3
# print(f"total cost: kes{total_price}")
# total_price=float(price) * int(quantity)
# print(f"total cost: kes{total_price}")

# # convert to float
# print(float(2))
# print(int(2.99))

# #Challenge 1: simple calculator
# # write a program that:
# # 1. take two numbers as inputs from the user
# a= int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# # 2. adds them together
# total= a+b
# # 3. print the results
# # print(total)
# print(f"the sum is: {total}")

# # challenge 2: temperature converter
# # write a program that:
# # 1. takes a temperature in Celcius as input
# temp=float(input("enter temp in Celcius:"))
# # 2. converts it to fahrenheit(formular: F=C * 9/5+32)
# result=(temp * 9/5+32)
# # print the results
# print(f"The fahrenheit is: {result}")

# # Challenge 3: Age calculator
# #write a program that:
# # asks for the user's birth year
# birth_year=int(input("enter birth year:"))
# # 2. calculates their age in 2025
# age=2025-birth_year
# result= (2025 - birth_year )
# # 3. prints how old they are/will be this year
# print(f"you are/will be this old: {result}")

# Challenge 4: Simple Interest Calculator
# write ap program that:
P= 20000
R= 0.15
T= 2
# 1. takes principal amount
P=(int(input("Enter principal: ")))
# 2. takes interest rate(as percentage)
R=(float(input("Enter the rate: ")))
# 3. takes time in years
T=(int(input("Enter the years: ")))
# 4. calculate simple interest using formular: find the formula SI = P × R × T
Interest= P*R*T
print(f"The Interest is {Interest}")
# 5.prints both interest and total amount A=P(1+R*T)
Amount=P*(1+R*T)
print(f"The amount is {Amount}")
# Next Booleans