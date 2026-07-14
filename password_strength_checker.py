import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    print("\nPassword Analysis")
    print("-" * 30)

    if score == 5:
        print("Strength : STRONG")
    elif score >= 3:
        print("Strength : MEDIUM")
    else:
        print("Strength : WEAK")

    print("\nSuggestions:")

    if len(password) < 8:
        print("- Use at least 8 characters.")

    if not re.search(r"[A-Z]", password):
        print("- Add at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        print("- Add at least one lowercase letter.")

    if not re.search(r"[0-9]", password):
        print("- Add at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add at least one special character.")

password = input("Enter your password: ")
check_password_strength(password)
