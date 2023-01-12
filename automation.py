file = open('assets/potential_contacts.txt', 'r')
content = file.read()
file.close()

with open('collected/emails.txt', 'w') as f:
    f.write('hello world')
