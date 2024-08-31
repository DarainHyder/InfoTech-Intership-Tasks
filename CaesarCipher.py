def encrypt(text, shift):
    result = ""
    
    # Traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Leave non-alphabetic characters as they are
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main code
if __name__ == "__main__":
    while True:
        # Take input from user
        text = input("Enter the text to be encrypted (or type 'quit' to exit): ")
        if text.lower() == 'quit':
            print("Exiting the program.")
            break
        
        shift = int(input("Enter the shift value: "))

        # Encrypt the text
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")

        # Decrypt the text
        decrypted_text = decrypt(encrypted_text, shift)
        print(f"Decrypted Text: {decrypted_text}")
