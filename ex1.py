class Rectangle:
    def __init__(self, length, width):
        """Initializes the rectangle with length and width."""
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def calculate_area(self):
        """Returns the area of the rectangle."""
        return self.length * self.width
rect_one = Rectangle(10, 5)
print(f"Rectangle 1 (10x5):")
print(f"Perimeter: {rect_one.calculate_perimeter()}")
print(f"Area:      {rect_one.calculate_area()}")
print("-" * 20)

rect_two = Rectangle(7.5, 3)
print(f"Rectangle 2 (7.5x3):")
print(f"Perimeter: {rect_two.calculate_perimeter()}")
print(f"Area:      {rect_two.calculate_area()}")