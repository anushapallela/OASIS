import random
import string
def generate_password(length=12):
    """Generate a random password of a given length."""
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    
    except ValueError:
        print("Please enter a valid numerical value for password length.")

if __name__ == "__main__":
    main()
