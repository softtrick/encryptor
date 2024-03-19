# Encrypt

from random import randint

def main():
    # Get plaintext user input
    plaintext = input("Enter plaintext: ")

    # Get key user input
    key = input("Enter key\n(type 'n' to generate a random key):\n")

    # If key is 'n', generate a random key
    if key == "n":
        key = str(randint(1000000000, 9999999999))
        
    cyphertext = encrypt(plaintext, key)
    print(f"Key: {key}")
    print(cyphertext)

# Define encrypt function
def encrypt(plaintext, key):
    cyphertext = ""
    n = 0
    # Convert each char in str key to an int in a list called key
    key = [int(n) for n in key]
    for char in plaintext:
        # If there are no more indexes in key, go back to start
        if n == len(key):
            n = 0
        cyphertext += chr(ord(char) + key[n])
        # Move to the next index in key
        n += 1
            
    return cyphertext


input("Press Enter to close...")

if __name__ == "__main__":
    main()
