class Rectangle(object):
    """
    a class that models width and height of a rectangle
    """

    def __init__(self):
        self.width = 0
        self.height = 0


def get_area(rec):

    return rec.width * rec.height


def main():
    rect1 = Rectangle()

    rect1.width = float(input("Enter the width: "))
    rect1.height = float(input("Enter the height: "))

    area = get_area(rect1)

    print("The area of the rectangle is " + str(area))
    print("The area of the rectangle is", area)

main()