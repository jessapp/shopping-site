"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
     
    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: %s, %s, %s, %s>" % (
            self.first_name, self.last_name, self.email, self.password)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: Customer object}
    """

    customers = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email,
         password) = line.strip().split("|")

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers


def get_by_email(email):
    """Return a customer, given their email."""

    # This relies on access to the global dictionary `customers`

    return customers.get(email)

# Dictionary to hold types of customers.
#
# Format is {email: Customer object, ... }

customers = read_customers_from_file("customers.txt")
