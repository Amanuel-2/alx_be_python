def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.
    Supported operations: add, subtract, multiply, divide
    Returns the result or an error message for invalid operations or zero division.
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

    else:
        return "Error: Invalid operation"
