# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 10


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#Simple if
if x > y:
  print(f'{x} is greater')

#if/else
if x > y:
  print(f'{x} is greater')
elif x == y:
  print('Theyre the same picture') 
else:
  print('nah player')




# Logical operators (and, or, not) - Used to combine conditional statements
if x > 2 and x <=10:
  print('something cool')

if x > 5 or x <= 7:
  print('another statement')

if not(x == y):
  print(f'{x} is not {y}')



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1 ,2, 3, 4, 5 ,10]

if x in numbers:
  print(x in numbers)


if x in numbers:
  print(x not in numbers)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
