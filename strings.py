# Strings (str) - Textual Data (is a collection of characters, for example alphabet letters, numbers and symbols, enclosed in single, double or triple quotes when spanning multiple lines)

# diffrent ways to craete string
single_quotes='Hello'
double_quotes="Hello"
triple_quotes ='''This is a multi-line string'''
triple_quotes= """This is a multi-line string"""
print(single_quotes)
print(double_quotes)
print(triple_quotes)
# check the type of the variable
print(type(single_quotes)) #<class 'str'>
print(type(double_quotes)) #<class 'str'>
print(type(triple_quotes)) #<class 'str'>

# string operations
name= 'Susan'

# finding out the number of characters in a string - we use the len()
print(len(name)) #returns 5

# convert a string to uppercase
print(name.upper()) #SUSAN

# convert a string to lowercase
print(name.lower()) #susan

# Next class -> Indexing and Slicing
