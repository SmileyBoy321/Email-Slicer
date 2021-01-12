"""
Python Project Idea – The email slicer is a handy program to get the username and domain name from an email address.

You can customize and send a message to the user with this information.
"""
import matplotlib.pyplot as plt
from setup_database import Database


def show_gmail_percentage():
    """Visualization of how many users use these domains in percentage"""
    database = Database()
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = "Gmail", "Yahoo", "Hotmail", "Aol"
    sizes = [database.count_domain_users("gmail.com"), database.count_domain_users("yahoo.com"),
             database.count_domain_users("hotmail.com"), database.count_domain_users("aol.com")]
    explode = (0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


if __name__ == '__main__':
    show_gmail_percentage()
