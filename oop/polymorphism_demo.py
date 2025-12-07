import math

class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """
        Calculate the area of the shape.
        This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape."""
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle with length and width.
        
        Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate and return the area of the rectangle.
        
        Returns:
        float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape."""
    
    def __init__(self, radius):
        """
        Initialize a Circle with radius.
        
        Parameters:
        radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate and return the area of the circle.
        
        Returns:
        float: The area (π × radius²)
        """
        return math.pi * (self.radius ** 2)