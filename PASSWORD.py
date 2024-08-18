import random
import string

def generate_password(length, uppercase, numbers, special_chars):
    """Generate a password of the specified length and complexity"""
    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("----------------")

    # Get user input
    length = int(input("Enter the desired length of the password: "))
    print("Reply with a YES/NO For the Following Questions.")
    uppercase = input("Do you want to include Uppercase alphabets?").lower() == 'yes'
    numbers = input("Do you want to include numbers?").lower() == 'yes'
    special_chars = input("Do you want to include characters?").lower() == 'yes'

    # Generate password
    password = generate_password(length, uppercase, numbers, special_chars)

    # Display password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
