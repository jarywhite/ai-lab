import random, string

def generate_password(length):
    """Return a random password of the given length."""
    pool = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        "!@#$%^&*()-_=+[]{}"
    )
    return "".join(random.choice(pool) for _ in range(length))

if __name__ == "__main__":
    print("🔐  Simple Password Generator")
    while True:
        user_input = input("Enter password length (e.g. 12): ")
        if user_input.isdigit() and int(user_input) > 0:
            length = int(user_input); break
        print("❌  Please enter a positive integer.")
    print("✅  Your password:", generate_password(length))
