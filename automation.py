import re
import shutil


def find_contact_info():
    file = open('assets/potential_contacts.txt', 'r')
    content = file.read()
    file.close()

    phone_seq = "([+]?[0-9]{1,3}[-| |.|])?([(][0-9]{3}[)]|[0-9]{3}[-| |.|])?([0-9]{3}[-| |.|][0-9]{4})(x[0-9]{1,5})*"
    phone_match = re.findall(phone_seq, content)

    with open('collected/phone_numbers.txt', 'w') as f:
        for match in phone_match:
            f.write("".join(match) + "\n")


if __name__ == "__main__":
    find_contact_info()
