def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def compute(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

def calculator():
    print("Welcome to the Python Calculator!")
    last_result = None

    operations = {
        '1': '+', '+': '+',
        '2': '-', '-': '-',
        '3': '*', '*': '*',
        '4': '/', '/': '/'
    }

    while True:
        print("\nOptions:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Quit (q)")
        if last_result is not None:
            print(f"(Current result: {last_result})")

        choice = input("Choose an operation or 'q' to quit: ").lower()

        if choice == 'q' or choice == '5':
            print("Goodbye!")
            break

        if choice in operations:
            op = operations[choice]

            # Decide on first number
            if last_result is None:
                num1 = get_number("Enter first number: ")
            else:
                use_last = input("Use last result as first number? (y/n): ").lower()
                num1 = last_result if use_last == 'y' else get_number("Enter first number: ")

            # Get second number (with division check)
            while True:
                num2 = get_number("Enter second number: ")
                if op == '/' and num2 == 0:
                    print("Cannot divide by zero. Enter a different number.")
                else:
                    break

            last_result = compute(num1, num2, op)
            print(f"Result: {last_result}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
