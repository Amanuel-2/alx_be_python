# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide).

    Args:
        num1: The first number.
        num2: The second number.
        operation: The arithmetic operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        The result of the arithmetic operation, or a string message
        if the operation is invalid or if a division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'."

if __name__ == "__main__":
    # Example usage for testing
    print(f"5 + 6 = {perform_operation(5, 6, 'add')}")
    print(f"10 - 3 = {perform_operation(10, 3, 'subtract')}")
    print(f"4 * 7 = {perform_operation(4, 7, 'multiply')}")
    print(f"20 / 4 = {perform_operation(20, 4, 'divide')}")
    print(f"10 / 0 = {perform_operation(10, 0, 'divide')}")
    print(f"Invalid op: {perform_operation(10, 2, 'power')}")
