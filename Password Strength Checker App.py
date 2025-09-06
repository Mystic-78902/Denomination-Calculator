import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (min 8 characters)": length_error,
        "Missing lowercase letter": lowercase_error,
        "Missing uppercase letter": uppercase_error,
        "Missing digit": digit_error,
        "Missing special character": special_char_error,
    }

    passed_checks = 5 - sum(errors.values())

    if passed_checks == 5:
        strength = "Very Strong "
    elif passed_checks == 4:
        strength = "Strong "
    elif passed_checks == 3:
        strength = "Moderate "
    elif passed_checks == 2:
        strength = "Weak "
    else:
        strength = "Very Weak "

    print("\nPassword Analysis:")
    for issue, failed in errors.items():
        if failed:
            print(f" {issue}")
        else:
            print(f" {issue}")

    print(f"\nPassword Strength: {strength}\n")


if __name__ == "__main__":
    while True:
        pwd = input("Enter a password to check (or type 'exit' to quit): ")
        if pwd.lower() == 'exit':
            break
        check_password_strength(pwd)
