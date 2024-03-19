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

    # Convert nun-numeric characters to unicode code points
    key = [int(ord(char)) if not char.isdigit() else int(char) for char in key]

    # Decrypt plaintext and print result
    plaintext = decrypt(cyphertext, key)
    print(f"\nPlaintext:\n{plaintext}\n")

    input("Press Enter to close...")
    
# Define decrypt function
def decrypt(cyphertext, key):
    plaintext = ""
    n = 0

    for char in cyphertext:

        # If there are no more indexes in key, go back to start
        if n == len(key):
            n = 0
            
        plaintext += chr(ord(char) - key[n])

        # Move to the next index in key
        n += 1

    return plaintext

if __name__ == "__main__":
    main()