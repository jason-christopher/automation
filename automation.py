import re
import shutil


def find_contact_info():
    file = open('assets/potential_contacts.txt', 'r')
    content = file.read()
    file.close()

    phone_seq = r"([+]?[0-9]{1,3}[-| |.|])?[(]?([0-9]{3})[)]?[-| |.]?([0-9]{3})[-| |.]?([0-9]{4})(x[0-9]{1,5})?"
    email_seq = r"\w*@\w*[-]?\w*.\w*"
    phone_match = re.findall(phone_seq, content)
    email_match = re.findall(email_seq, content)

    with open('collected/phone_numbers.txt', 'w') as f:
        for match in phone_match:
            phone_num = str(match[1]) + "-" + str(match[2]) + "-" + str(match[3]) + str(match[4])
            f.write(phone_num + "\n")

    with open('collected/emails.txt', 'w') as f:
        for match in email_match:
            f.write(match + "\n")


if __name__ == "__main__":
    find_contact_info()
