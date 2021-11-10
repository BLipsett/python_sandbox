# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create Class
class User:
  #Constructor function that runs wehen you instantiate an object from a class
  def __init__(self, name, email, age) -> None:
      self.name = name
      self.email = email
      self.age = age

  def greeting(self):
    return f'my name is {self.name}'

  def addBirthday(self):
    self.age += 5


class Customer(User):
  #Constructor function that runs wehen you instantiate an object from a class
  def __init__(self, name, email, age) -> None:
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0
  
  def getBalance(self, balance):
    self.balance = balance

  def greeting(self):
      return super().greeting()


#init user obj
brian = User('Brian', 'Brain@gmail.com', 45)


brian.addBirthday()
print(brian.age)

james = Customer('James', 'James@gmail.com', 25)

print(james.greeting())

