import re


def find_contact_info():
    # pulls information from the Potential Contacts file
    file1 = open('assets/potential_contacts.txt', 'r')
    content = file1.read()
    file1.close()

    # stretch goal - pulls information from the Existing Contacts file
    file2 = open('assets/existing-contacts.txt', 'r')
    existing = file2.read()
    file2.close()

    # clears out anything in the emails.txt and phone_numbers.txt files
    open("collected/emails.txt", 'w').close()
    open("collected/phone_numbers.txt", 'w').close()

    phone_seq = r"([+]?\d{1,3}[-| |.|])?[(]?(\d{3})[)]?[-| |.]?(\d{3})[-| |.]?(\d{4})(x\d{1,5})?"
    email_seq = r"\w*@\w*[-]?\w*.\w*"
    phone_match = sorted(set(re.findall(phone_seq, content)))
    email_match = sorted(set(re.findall(email_seq, content)))

    with open('collected/phone_numbers.txt', 'w') as f:
        for match in phone_match:
            phone_num = str(match[1]) + "-" + str(match[2]) + "-" + str(match[3]) + str(match[4])
            if phone_num not in existing:
                f.write(phone_num + "\n")

    with open('collected/emails.txt', 'w') as f:
        for match in email_match:
            if match not in existing:
                f.write(match + "\n")


if __name__ == "__main__":
    find_contact_info()
