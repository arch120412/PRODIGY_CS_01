def caesar_cipher_encrypt(text, shift):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text:
        if char.isupper():
            index = uppercase.index(char)
            new_index = (index + shift) % 26
            encrypted_text += uppercase[new_index]
        elif char.islower():
            index = lowercase.index(char)
            new_index = (index + shift) % 26
            encrypted_text += lowercase[new_index]
        else:
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''

    for char in text:
        if char.isupper():
            index = uppercase.index(char)
            new_index = (index - shift + 26) % 26
            decrypted_text += uppercase[new_index]
        elif char.islower():
            index = lowercase.index(char)
            new_index = (index - shift + 26) % 26
            decrypted_text += lowercase[new_index]
        else:
            decrypted_text += char

    return decrypted_text

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? Please enter 'e' to encrypt or 'd' to decrypt : ").lower()
        if choice in ['e', 'd']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                print("Encrypted message:", caesar_cipher_encrypt(message, shift))
            else:
                print("Decrypted message:", caesar_cipher_decrypt(message, shift))
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        
        continue_choice = input("Do you want to process another message? (yes/no): ").lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()

