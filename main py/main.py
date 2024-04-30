"""
Author: Surya Pratap Singh Chauhan
GitHub: https://github.com/brodante
Email: surya.pratap0038@gmail.com
Website: https://brodante.github.io/portfolio/

Description: final year college student stuck in an infinite loop.
"""
# main.py

import identifyhash
import hashify

def identify_hash():
    identifyhash.identify_hash()
def encrypt():
    hashify.hashify()
    print("Encryption function")

def decrypt():
    # Implement decryption logic here
    print("Decryption function")

def exit_program():
    print("Exiting...")
    exit()

def main():
    while True:
        print("\nMenu:")
        print("1. Identify Hash")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            identify_hash()
        elif choice == "2":
            encrypt()
        elif choice == "3":
            decrypt()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
