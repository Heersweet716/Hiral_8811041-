# test_number_operations.py
import number_operations


def test_smallest_number():
    numbers = [2, 4, 6, 1, 8]
    assert number_operations.is_smallest(1, numbers) is True


def test_not_smallest_number():
    numbers = [2, 4, 6, 1, 8]
    assert number_operations.is_smallest(6, numbers) is False
