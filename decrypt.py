# Decrypt

def main():
    # Get cyphertext user input
    cyphertext = ""
    while not cyphertext:
        cyphertext = input("Enter cyphertext:\n")

    # Get key user input
    key = ""
    while not key:
        key = input("\nEnter key:\n")

    # Decrypt cyphertext using key
    plaintext = decrypt(cyphertext, key)

    # Print result
    print(f"\nPlaintext:\n{plaintext}\n")
    input("Press Enter to close...")
    
# Define decrypt function
def decrypt(cyphertext, key):
    
    # Convert nun-numeric characters to unicode code points
    key = "".join((str(ord(char)) if not char.isdigit() else char for char in key))

    # Convert each char in str key to an int in a list called key
    key = [int(char) for char in key]

    # Define variables for plaintext string and n for iterations of the loop
    plaintext = ""
    n = 0
    for char in cyphertext:

        # If there are no more indexes in key, go back to start
        if n == len(key):
            n = 0

        # Decrypt cyphertext using key
        plaintext += chr(ord(char) - key[n])

        # Move to the next index in key
        n += 1

    return plaintext

if __name__ == "__main__":
    main()
