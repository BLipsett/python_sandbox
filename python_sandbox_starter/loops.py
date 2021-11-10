# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Brian', 'John', 'Paul', 'Sara']

for person in people:
  print(f'current person: {person}')


for person in people:
  if person == 'Sara':
    break
  print(f'Im: {person}')


for person in people:
  if person == 'John':
    continue
  print(f'person is {person}')


for i in range(len(people)):
  print(people[i])

for i in range(0, 11):
  print(f"Number: {i}")


# While loops execute a set of statements as long as a condition is true.

count = 0

while count <=10:
  print(f'count: {count}')
  count += 1