# 🧮 Error-Proof Calculator
# This calculator safely handles any invalid input using try-except blocks.

def get_number(prompt):
    """Safely input a number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def calculate(num1, num2, operator):
    """Performs calculation with error handling."""
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            raise ValueError("Unsupported operator. Use +, -, *, or /")
    except ZeroDivisionError:
        print("❌ Division by zero is not allowed.")
        return None
    except Exception as e:
        print("⚠️ Unexpected error:", e)
        return None

def main():
    print("🔹 Welcome to the Error-Proof Calculator 🔹")

    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operator = input("Enter operator (+, -, *, /): ")

        result = calculate(num1, num2, operator)
        if result is not None:
            print(f"✅ Result: {result}")

        again = input("\nDo you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Goodbye! Stay error-free.")
            break

if __name__ == "__main__":
    main()
