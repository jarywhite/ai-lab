# =================================================
# Mini-Project #1: Simple CLI Calculator
# =================================================

def get_number(prompt):
    """
    Repeatedly ask the user for input until they type a valid number.
    Returns the number as a float.
    """
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("❌ Please enter a valid number, e.g. 12.5")

def main():
    print("🔢 Simple CLI Calculator")
    # 1. Gather two numbers from the user
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # 2. Show operation choices
    print("Choose operation:")
    print(" 1) Add (+)")
    print(" 2) Subtract (-)")
    print(" 3) Multiply (×)")
    print(" 4) Divide (÷)")
    op = input("Enter 1, 2, 3, or 4: ")

    # 3. Compute based on the choice
    if op == "1":
        result = num1 + num2  # addition
    elif op == "2":
        result = num1 - num2  # subtraction
    elif op == "3":
        result = num1 * num2  # multiplication
    elif op == "4":
        if num2 == 0:
            print("❌ Cannot divide by zero.")
            return          # exit early on error
        result = num1 / num2  # division
    else:
        print("❌ Invalid operation selection.")
        return              # exit early on error

    # 4. Show the result
    print(f"✅ Result: {result}")

# Standard Python boilerplate to run main() only when this file is executed
if __name__ == "__main__":
    main()
