# Python has functions for creating, reading, updating, and deleting files.
#OPen a file 

myFile = open('myfile.txt', 'w')

#Get info
print('Name: ', myFile.name)
print('Name: ', myFile.closed)
print('Name: ', myFile.mode)

myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

#Append to file 
myFile = open('myFile.txt', 'a')
myFile.write('PHP is lame')

