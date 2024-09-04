"""
Library: Password Generator
Author: Haluk YAMANER
Email: haluk@halukyamaner.com
Web: https://www.halukyamaner.com
Version: 1.0

Description:
    This script generates secure random passwords of a specified length using alphanumeric characters 
    (letters and digits). The user can input the number of passwords they would like to generate, 
    and the script will display each password. The default length of each password is 36 characters.

Usage:
    The script is executed from the command line. The user is prompted to enter the number of passwords 
    they want to generate. The passwords will be displayed in the terminal, using a combination of 
    letters and digits without any special characters.

Requirements:
    Python 3.x
    Modules: random, string

Features:
    - Generates random passwords consisting of uppercase, lowercase letters, and digits
    - The default length for each password is 36 characters
    - User can generate multiple passwords in one run

Warnings:
    - No special characters are used in the generated passwords.
    - Ensure the generated passwords are stored securely after creation.
"""
import random
import string

def generate_password(length=36):
    # Define the character set for the password (no special characters)
    characters = string.ascii_letters + string.digits
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to input the number of passwords to generate
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        if num_passwords <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Generate and display the requested number of passwords
    for i in range(num_passwords):
        print(f"Password {i + 1}: {generate_password()}")

if __name__ == "__main__":
    main()
