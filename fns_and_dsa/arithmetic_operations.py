def perform_operation(num1: float, num2: float, operation: str):
    """Perform a basic arithmetic operation on two numbers.

    Supported operations (operation must be provided as lower-case string):
      - 'add'      -> returns num1 + num2
      - 'subtract' -> returns num1 - num2
      - 'multiply' -> returns num1 * num2
      - 'divide'   -> returns num1 / num2 or a string error message for division by zero

    Returns:
      - float: when operation completes successfully
      - str: an error message when the operation is invalid or when dividing by zero
    """

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            # Return a clear string the caller can detect and display
            return "Error: Division by zero"
        return num1 / num2

    return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'."

def main():
    print("Arithmetic operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()