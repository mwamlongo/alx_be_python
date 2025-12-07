class Calculator:
    """A calculator class demonstrating class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not need access to class or instance data.
        
        Parameters:
        a (int/float): First number
        b (int/float): Second number
        
        Returns:
        int/float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Has access to class attributes via cls parameter.
        
        Parameters:
        cls: Reference to the class itself
        a (int/float): First number
        b (int/float): Second number
        
        Returns:
        int/float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b