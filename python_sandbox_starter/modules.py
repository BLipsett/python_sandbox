# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core modules 
import datetime
from datetime import date
import time 
from time import time 

#Pip module - like node for installing npm packages
from camelcase import CamelCase

#Import custom module
import validator
from validator import validate_email


today = datetime.date.today()
now = date.today()
timeStamp = time()

print(today)
print(now)
print(timeStamp)

c = CamelCase()
print(c.hump('hello to the whole world'))

email = 'test3test.com'

if validate_email(email):
  print(f'{email} is valid')
else:
  print('nah it sux')

