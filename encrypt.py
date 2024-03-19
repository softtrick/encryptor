# Encrypt

from random import randint

def main():
    # Get plaintext user input
    plaintext = input("Enter plaintext:\n")

    # Get key user input
    key = ""
    while not key:
        key = input("\nEnter key\n(type 'n' to generate a random key):\n")

    # If key is 'n', generate a random key
    if key == "n":

        # if plaintext is empty generate set key length to 10
        length = len(plaintext) if plaintext else 10

        # Generate random key
        numeric_key = [randint(1, 9) for _ in range(length)]
        key = "".join(map(str, numeric_key))
        
    # Convert nun-numeric characters to unicode code points
    else:
        numeric_key = [ord(char) if not char.isdigit() else int(char) for char in key]
        
    cyphertext = encrypt(plaintext, numeric_key)
    print(f"\nKey:\n{key}\n")
    print(f"Cyphertext:\n{cyphertext}\n")
    
    input("Press Enter to close...")

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

if __name__ == "__main__":
    main()
