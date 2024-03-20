# Encrypt

from random import randint

def main():
    # Get plaintext user input
    plaintext = input("Enter plaintext:\n").strip()

    # Get key user input
    key = ""
    while not key:
        key = input("\nEnter key\n(type 'n' to generate a random key):\n").strip()

    # If key is 'n', generate a random key
    if key == "n":
        # if plaintext is empty generate set key length to 10
        key = generate_key(len(plaintext) if plaintext else 10)

    # Encrypt plaintext using key
    cyphertext = encrypt(plaintext, key)

    # Print result and key
    print(f"\nKey:\n{key}\nCyphertext:\n{cyphertext}\n")
    input("Press Enter to close...")

# Define generate key function
def generate_key(length):
    
    # Generate random key
    return ''.join(str(randint(0, 9)) for _ in range(length))

# Define encrypt function
def encrypt(plaintext, key):

    # Convert nun-numeric characters to unicode code points
    key = "".join((str(ord(char)) if not char.isdigit() else char for char in key))

    # Convert each char in str key to an int in a list called key
    key = [int(char) for char in key]

    # Define variables for cyphertext string and n for iterations of the loop
    cyphertext = ""
    n = 0
    for char in plaintext:
        
        # If there are no more indexes in key, go back to start
        if n == len(key):
            n = 0
            
        # Encrypt plaintext using key
        cyphertext += chr(ord(char) + key[n])
        
        # Move to the next index in key
        n += 1
            
    return cyphertext

if __name__ == "__main__":
    main()
