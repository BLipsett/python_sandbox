# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""


'''
Main types of variables '''


x = 1  #int 
y = 2.5  #float
name = 'john'  #string 
is_cool = True # boolean

# Multiple assignments
x, y, name, is_cool = (1, 2, 'john', False)

#Basic math
a = x + y

#casting 
a = str(a)
y = int(y)

print(type(a))