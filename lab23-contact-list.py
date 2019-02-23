"""
Build a program to manage a list of contacts. To start, we'll build a CSV
('comma separated values') together, and go over how to load that file.
Headers might consist of name, favorite fruit, favorite color. Open the CSV,
convert the lines of text into a list of dictionaries, one dictionary for each
user. The text in the header represents the keys, the text in the other lines
represent the values.

"""


def load(csv):
    with open(csv) as file:
        lines = file.read().split('\n')

    contacts = []
    keys = lines[0].split(',')

    for i in range(1, len(lines)):
        entry = lines[i].split(',')
        entry = dict(zip(keys, entry))
        contacts.append(entry)
    return (contact_list, props)


def find_contact(contact_list, name):
    """
    return the index of a contact in contact_list with the matching name
    """
    for i in range(len(contact_list)):
        contact = contact_list[i]
        if contact["name"] == name:
            return i


def create(contact_list, contact):
    """
    Create a record: ask the user for each attribute,
    add a new contact to your contact list with the
    attributes that the user entered.
    """

    index = find_contact(contact_list, contact['name'])
    if index is not None:
        return f"Error: {contact['name']} already exists"
    contact_list.append(contact)
    return f"Created contact for {contact['name']}."


def read(contact_list, name):
    """
    Retrieve a record: ask the user for the contact's name,
    find the user with the given name, and display their information
    index = find_contact(contact_list, name)

    """
    index = find_contact(contact_list, name)
    if index is None:
        return f"Error: {'name'} does not exist!"

    return contact_list[index]


def update(contact_list, name, updated_info):
    """
    Update a record: ask the user for the contact's name,
    then for which attribute of the
    user they'd like to update and
    the value of the attribute they'd like to set.
    """

    index = find_contact(contact_list, name)
    if index is None:
        return f"Error: {'name'} does not exist!"
    contact_list[index].update(updated_info)
    return f"updated contact for {"name"}"


def delete(contact_list, name):
    """
    Delete a record: ask the user for the contact's name,
    remove the contact with the given name from the contact list.
    """

    index = find_contact(contact_list, name)
    if index is None:
        return f"Error: {'name'} does not exist!"

    contact_list.pop(index)
    return f"{'name'} deleted."


def save(contact_list, header, csv):
    """
    takes the list of contacts to be saved and a filepath
    """
    contacts = [','.join(header)]
    for contact in contact_list:
        contacts.append(','.join(contact.values()))
    with open(csv, 'w') as f:
        f.write('\n'.join(contacts))
    return f'Saving contacts as {csv}...'


def print_contact(contact):
    """
    pretty prints a single contacts
    """
    if type(contact) is dict:
        for k, v in contact.items():
            print(f"{'k'}: {'v'}")
        else:
            print(contact)


def list_all(contact_list):
    """
    pretty prints all the contacts
    """
    for contact in contact_list:
        print_contact(contact)
        print()


if __name__ == '__main__':
    contacts, props = load('contact_list.csv')
    loop = True
    valid_inputs = [
        'c', 'create',
        'r', 'read',
        'u', 'update',
        'd', 'delete',
        'e', 'list', 'ls',
        'x', 'exit', 'quit',
        'h', 'help'
    ]
    commands = """
        Commands:
        (c)reate
        (r)ead
        (u)pdate
        (d)elete
        (e)xpand list
        e(x)it
        (h)elp
    """

    print('Welcome to your contact list')
    print(commands)

    while loop:
        print('-'*60)
        valid = False

        while not valid:
            cmd = input('cmd> ').strip().lower()
            if cmd in valid_inputs:
                valid = True
            else:
                print('Invalid input.')
                print(commands)

        if cmd in ['x', 'exit', 'quit']:
            # save contacts as csv
            print(save(contacts, props, 'contact_list.csv'))
            loop = False
            print('Goodbye!')

        elif cmd in ['e', 'list', 'ls']:
            list_all(contacts)

        elif cmd in ['h', 'help']:
            print(commands)

        elif cmd.startswith('c'):
            contact = {}
            for prop in props:
                contact[prop] = input(f'{prop}: ')
            print(create(contacts, contact))

        else:
            name = input('name: ')

            # if name not in contact_list, prompt user to create one instead
            index = find_contact(contacts, name)
            if index is None:
                print('Error:', name, 'does not exist.')

                if not cmd.startswith('d'):
                    create_instead = input(f'Do you want to create a contact for {name}? ').strip().lower()
                    if create_instead in ['y', 'yes']:
                        contact = {}
                        for prop in props:
                            contact[prop] = input(f'{prop}: ')
                        print(create(contacts, contact))
                continue

            print('-'*60)

            if cmd.startswith('r'):
                contact = read(contacts, name)
                print_contact(contact)

            elif cmd.startswith('u'):
                contact = {}
                for prop in props:
                    val = input(f'{prop}: ')
                    if val:
                        contact[prop] = val
                print(update(contacts, name, contact))

            elif cmd.startswith('d'):
                confirmation = input('are you sure? ').strip().lower()
                if confirmation in ['y', 'yes']:
                    print(delete(contacts, name))
                else:
                    print('Aborting...')
