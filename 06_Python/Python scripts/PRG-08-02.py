import csv
myfile = open("gegevens.csv", "r+")
print(myfile.read())


thisdict = {
    
}


thisdict["First name"] = input("Je voornaam:")
thisdict["Last name"] = input("Je achternaam:")
thisdict["Job Title"] = input("Je Job Title:")
thisdict["Company"] = input("Company naam:")

print("The dictionary is:")
print(thisdict)

writer = csv.writer(myfile)
writer.writerow(thisdict.values())
myfile.close()
myfile = open('gegevens.csv', 'r')
print("The content of the csv file after appending is:")
print(myfile.read())