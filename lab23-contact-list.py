"""
Build a program to manage a list of contacts. To start, we'll build a CSV
('comma separated values') together, and go over how to load that file.
Headers might consist of name, favorite fruit, favorite color. Open the CSV,
convert the lines of text into a list of dictionaries, one dictionary for each
user. The text in the header represents the keys, the text in the other lines
represent the values.

"""

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []
keys = lines[0].split(',')

for i in range(1, len(lines)):
	entry = lines[i].split(',')
	entry = dict(zip(keys, entry))
	contacts.append(entry)


"""
Create a record: ask the user for each attribute, 
add a new contact to your contact list with the attributes that the user entered.
"""
name = input("Enter a name to add to your contacts: ")
phone = input("What's their phone number?: ")
city = input("What city do they live in?: ")

contacts.append({'name': name, 'phone': phone, 'city': city})


"""
Retrieve a record: ask the user for the contact's name, 
find the user with the given name, and display their information
"""
retriever =  input("What is the contacts name you want to retrieve?: ")
for i in contacts:
	if i["name"] == retriever:
		print(i)


"""
Update a record: ask the user for the contact's name, then for which attribute of the 
user they'd like to update and the value of the attribute they'd like to set.
"""
contact_update = input("What's the contact's name that you want to update?: ")
attribute = input("Which attribute do you want to update (name, phone, city)?: ")
attribute_value = input("What should it be replaced by?: ")

for i in contacts:
	if i["name"] == contact_update:
		i[attribute] = attribute_value
		print(i)


"""
Delete a record: ask the user for the contact's name, 
remove the contact with the given name from the contact list.
"""

del_contact = input("Which contact do you want to remove?: ")
for index, i in enumerate(contacts):
	if i["name"] == del_contact:
		del contacts[index]
		print(contacts)
