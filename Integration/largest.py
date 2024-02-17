def is_largest(number, number_list):
    """
    Check if a number is the largest among a list of numbers.
    
    Args:
        number (int): The number to be checked.
        number_list (list): A list of numbers.
        
    Returns:
        bool: True if the number is the largest, False otherwise.
    """
    return number == max(number_list)

