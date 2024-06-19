def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract second number from the first."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide first number by the second. Raise error if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    print("Simple Calculator Program")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input for numbers and operator
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        
        # Perform the calculation based on the operator
        if operator == '+':
            result = add(number1, number2)
        elif operator == '-':
            result = subtract(number1, number2)
        elif operator == '*':
            result = multiply(number1, number2)
        elif operator == '/':
            result = divide(number1, number2)
        else:
            print("Invalid operator! Please enter one of +, -, *, /.")
            return

        # Print the result
        print(f"The result of {number1} {operator} {number2} is: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")

# Call the main function
if __name__ == "__main__":
    main()
