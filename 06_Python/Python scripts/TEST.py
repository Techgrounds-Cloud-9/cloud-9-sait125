import csv

myFile = open('gegevens.csv', 'r+')
print("The content of the csv file before appending is:")
print(myFile.read())
myDict = {'Roll': 4, 'Name': 'Joel', 'Language': 'Golang'}
print("The dictionary is:")
print(myDict)
writer = csv.writer(myFile)
writer.writerow(myDict.values())
myFile.close()
myFile = open('gegevens.csv', 'r')
print("The content of the csv file after appending is:")
print(myFile.read())