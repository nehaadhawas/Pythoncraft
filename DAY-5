# Simple Calculator using match statement in Python

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        match choice:
            case 1:
                result = num1 + num2
                operation = "Addition"
            case 2:
                result = num1 - num2
                operation = "Subtraction"
            case 3:
                result = num1 * num2
                operation = "Multiplication"
            case 4:
                if num2 != 0:
                    result = num1 / num2
                    operation = "Division"
                else:
                    return "Error: Division by zero is not allowed."
            case _:
                return "Invalid choice. Please enter a number between 1 and 4."

        return f"{operation} of {num1} and {num2} is {result}"
    except ValueError:
        return "Invalid input. Please enter numeric values."

if __name__ == "__main__":
    print(calculator())
