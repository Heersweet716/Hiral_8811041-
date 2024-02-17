# number_operations.py

def is_smallest(number, numbers):
    """
    Check if a number is the smallest in a list of numbers.

    Args:
        number (int): The number to be checked.
        numbers (list): A list of numbers.

    Returns:
        bool: True if the number is the smallest, False otherwise.
    """
    return number == min(numbers)
