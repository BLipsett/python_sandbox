# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'brian'
age = 29


# String Formatting
print('Hello, my name is ' + name + ', I am ' + str(age))


# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F strings
print(f'Hello my name is {name} and i am {age}')

s = "hello world"

# String Methods
print(s.capitalize())