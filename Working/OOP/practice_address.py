class Address(object):
    """
    a class that models the attributes of an address
    """

    def __init__(self):
        self.line1 = ""
        self.line2 = ""
        self.postalcode = ""
        self.city = ""
        self.province = ""
        self.country = "Canada"


def print_address(addr):
    print(addr.line1)
    if addr.line2 != "":
        print(addr.line2)
    print(addr.city + ", " + addr.province + ", " + addr.postalcode)
    print(addr.country)


def main():
    homeAddress = Address()
    workAddress = Address()

    homeAddress.line1 = "3266 Weston Road"
    homeAddress.line2 = "Apt #408"
    homeAddress.postalcode = "M9M 2V2"
    homeAddress.city = "Toronto"
    homeAddress.province = "Ontario"

    workAddress.line1 = "8101 Leslie Street"
    workAddress.postalcode = "L3T 4P7"
    workAddress.city = "Thornhill"
    workAddress.province = "Ontario"

    print("***HOME ADDRESS***")
    print_address(homeAddress)

    print("")

    print("***WORK ADDRESS***")
    print_address(workAddress)


main()