import csv
from random import randint


def grab_data_csv():
    """Function puts list of first and last names plus email domains from CSV file into three different lists"""
    first_name = []
    last_name = []
    email_domain = []

    with open("Full_email_list.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            first_name.append(row[0])
            last_name.append(row[1])
            email_domain.append(row[2])
    first_name.remove("First name")
    last_name.remove("Last name")
    email_domain.remove("Domain")
    return first_name, last_name, email_domain


def first_name():
    """Returns the first name like Jack"""
    return grab_data_csv()[0][randint(0, 98)]


def last_name():
    """Returns the last name like Sparrow"""
    return grab_data_csv()[1][randint(0, 98)]


def email_domain():
    """Returns the email domain for example gmail.com"""
    return grab_data_csv()[2][randint(0, 98)]


def email_address():
    """Function full email address like JackSparrow@gmail.com"""
    return first_name() + last_name() + "@" + email_domain()


"""
I don't know whether this function is needed or not. Let it stay like that for now.
def accounts_for_database():
    """'Make thousands of accounts for the database'"""
    accounts = []
    for i in range(1000):
        accounts.append(email_address())
    return accounts
"""


if __name__ == '__main__':
    pass
    #  print(accounts_for_database())
