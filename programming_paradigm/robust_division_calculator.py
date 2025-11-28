def safe_divide(numerator, denominator):
    """
    Safely perform division with error handling.
    
    Parameters:
    numerator: The dividend (can be string or number)
    denominator: The divisor (can be string or number)
    
    Returns:
    str: Result message or error message
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."