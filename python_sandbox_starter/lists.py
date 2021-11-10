# A List is a collection which is ordered and changeable. Allows duplicate members.
# MUCH LIKE ARRAYS IN JAVASCRIPT
# 0 based

# create list
numbers = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'grapes', 'pears']

#Use a constructor 
numbers2 = list((1, 2, 3, 4, 5))

print(fruits[1])

print(len(fruits))

fruits.append('mangoes')

fruits.remove('pears')

fruits.insert(1, 'strawberries')

fruits.pop(2)

fruits.reverse()

fruits.sort()

fruits[0] = 'blueberries'
print(fruits)