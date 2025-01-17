from cryptography.fernet import Fernet
import json
import os

# Generate a new encryption key (only needed once)
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

# Load the existing encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Add a new password
def add_password(website, username, password):
    encrypted_password = fernet.encrypt(password.encode()).decode()
    new_entry = {"username": username, "password": encrypted_password}
    
    # Load existing passwords
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}
    
    passwords[website] = new_entry

    # Save updated passwords
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)
    print(f"Password for {website} added successfully!")

# View saved passwords
def view_passwords():
    if not os.path.exists("passwords.json"):
        print("No passwords stored yet!")
        return

    with open("passwords.json", "r") as file:
        passwords = json.load(file)
    
    for website, credentials in passwords.items():
        username = credentials["username"]
        password = fernet.decrypt(credentials["password"].encode()).decode()
        print(f"Website: {website}\nUsername: {username}\nPassword: {password}\n")

# Main program
if __name__ == "__main__":
    generate_key()  # Generate key if not already generated
    key = load_key()
    fernet = Fernet(key)
    
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(website, username, password)
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
