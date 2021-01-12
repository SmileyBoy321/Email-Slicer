from tinydb import TinyDB, Query
#  from read_csv_file import first_name, last_name, email_domain, email_address
#  Remove the comment from above line if you need it to insert more accounts to database


class Database:
    """Database setup application"""

    def __init__(self):
        self.db = TinyDB("db.json")

    def email_to_database(self, firstname, lastname, domain, email_address):
        """Puts function parameters into the database to have a collection of emails"""
        self.db.insert({"Name": firstname,
                        "Surname": lastname,
                        "Domain": domain,
                        "Email_address": email_address})

    def count_domain_users(self, email_domain):
        """Returns the count of gmail users"""
        query = Query()
        count = 0
        for i in self.db.search(query.Domain == email_domain):
            count += 1
        return count


def main():
    """All instructions for database execution located in here"""
    #  database = Database()
    #  Make thousands of accounts for the database
    #  Uncomment the for loop if you need or want to append more accounts to database and indent correctly as well
    #  for i in range(1000):
    #  database.email_to_database(first_name(), last_name(), email_domain(), email_address())


if __name__ == '__main__':
    pass
    #  main()
