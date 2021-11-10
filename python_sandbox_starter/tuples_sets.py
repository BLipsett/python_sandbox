# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

print(fruits)

# A Set is a collection which is unordered and unindexed. No duplicate members.
#Create set

fruits_set = {'Apples', 'Oranges', 'Strawberries'}

print(fruits_set)
fruits_set.add('Grapes')
print('Apples' in fruits_set)