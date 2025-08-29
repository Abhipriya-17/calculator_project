# This calculator is structured using a class, which is a more organized approach
# for larger or more complex applications.

class Calculator:
    """
    A simple command-line calculator that performs basic arithmetic operations.
    """
    def __init__(self):
        """Initializes the calculator with a dictionary of operations."""
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
        }

    def add(self, x, y):
        """Adds two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtracts two numbers."""
        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers."""
        return x * y

    def divide(self, x, y):
        """Divides two numbers. Handles division by zero."""
        if y == 0:
            return "Error! Division by zero is not allowed."
        return x / y

    def run(self):
        """
        Main method to run the calculator loop, handling user input and
        performing calculations.
        """
        print("Welcome to the simple Python calculator!")
        print("Available operations: +, -, *, /")
        
        while True:
            try:
                # Get the first number from the user
                num1 = float(input("Enter the first number: "))
                
                # Get the operator from the user
                operator = input("Enter the operator (+, -, *, /) or 'q' to quit: ")
                
                # Check if the user wants to quit
                if operator.lower() == 'q':
                    print("Exiting the calculator. Goodbye!")
                    break
                
                # Check if the operator is valid
                if operator not in self.operations:
                    print("Invalid operator. Please use one of +, -, *, /")
                    continue
                    
                # Get the second number from the user
                num2 = float(input("Enter the second number: "))

                # Get the correct function from the dictionary and call it
                operation_function = self.operations[operator]
                result = operation_function(num1, num2)
                
                print(f"The result is: {result}")
            
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
