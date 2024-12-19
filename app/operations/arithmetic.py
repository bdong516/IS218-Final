from app.operations import Operation
from typing import Union

class add(Operation):
    """Class to perform addition of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Add two numbers.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a + b

class subtract(Operation):
    """Class to perform subtraction of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Subtract the second number from the first.

        Args:
            a (Union[int, float]): The minuend.
            b (Union[int, float]): The subtrahend.

        Returns:
            float: The difference of the two numbers.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a - b

class multiply(Operation):
    """Class to perform multiplication of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Multiply two numbers.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The product of the two numbers.
        """
        self._validate_inputs(a, b)  # Validate inputs
        return a * b

class divide(Operation):
    """Class to perform division of two numbers."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide the first number by the second.

        Args:
            a (Union[int, float]): The numerator.
            b (Union[int, float]): The denominator.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If the denominator (b) is zero.
        """
        self._validate_inputs(a, b)  # Validate inputs
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b