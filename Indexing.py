#slicing-extracting a portion or part of a string
# syntax-> variable_name[start_index:stop_index]
# slice 'Ali' from Alice
name = 'Alice'
print (name[0:3])

# slice 'ice'
print(name[2:5])
print(name[:5])
print(name[0:])
print(name[:])

#step- variable_name[start:stop:step]
#use negative index as a step to reverse a string
print(name[::-1])
print(name[0:5:-1])

#skip the second character using a step
print(name[::2])

#slicing methods
text=' Hello, World! '
#remove white space -strip()
print(text)
print(text.strip())

#replace text-replace()
print(text.replace('Hello','Hi')) #return Hi, World!
      
      #count the occurrence of a character -count()
print(text.count('o')) #2
      
      #find the index of a character-index()
print(text.index('d')) #12
      
      #split a string into a list-[] -split[]
print(text.split(',')) #return[' Hello', 'World! ']
      
      #join a string to a character or symbol
course_name='Python Data Visualization'
print('_'.join(course_name)) #P_y_t_h_o_n_ _D_a_t_a_ _V_i_s_u_a_l_i_z_a_t_i_o_n

#string formatting
name='Susan'
age= 25

#1. Using f-strings(Recommended)
print(f'My name is {name} and I am{age} years old')
#2. Using.format()
print('My name is {} and  I am {} years old'.format(name, age))

#3. Using % operator (older style)
#print('My name is %s and I am %d years old' (name, age))
print("My name is %s and I am %d years old" % (name, age))
