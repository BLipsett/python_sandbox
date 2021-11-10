# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


person = {
  'first_name' : 'John',
  'last_name' : 'Doe',
  'age' : 65
}

#Create with constructor
person2 = dict(first_name='sara', last_name='williams')


print(person.get('last_name'))

#Add to dictionary 
person['phone'] = '555-5656-8989'


#get dict keys
print(person.keys())


person3 = person.copy()
person3['City'] = 'Boston'


print(person)
print(person3)