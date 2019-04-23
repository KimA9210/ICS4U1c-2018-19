class Rectangle (object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def get_area(self, rec):

        """
        Computes the area of a rectangle
        :param rec: a Rectangle object
        :return: area of rec
        """
        return self.width * self.height

def main():

    user_width = float(input("Enter a width: "))
    user_height = float(input("Enter a height: "))

    rect1 = Rectangle()
    rect1.width = user_width
    rect1.height = user_height

    area = rect1.get_area(rect1)

    print("The area of the rectangle is " + str(area))

main()

//hellooo