import random

# List of alphabets
alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# Generate random key
def generateKey(length):
    return "".join([random.choice(alphabet_list) for i in range(length)])


# OTP encryption
def encrypt(plain_text, key):
    plain_text_indexes = []
    key_indexes = []

    # Get the index of each character of the plain text and key
    for i in range(len(plain_text)):
        plain_text_indexes.append(alphabet_list.index(plain_text[i]))
        key_indexes.append(alphabet_list.index(key[i]))

    # Sum indexes and apply modulo 26
    cipher_text_indexes = [
        (a + b) % 26 for a, b in zip(plain_text_indexes, key_indexes)
    ]

    # Get the character from the index
    return "".join([alphabet_list[index] for index in cipher_text_indexes])


# OTP decryption
def decrypt(cipher_text, key):
    cipher_text_indexes = []
    key_indexes = []

    for i in range(len(cipher_text)):
        cipher_text_indexes.append(alphabet_list.index(cipher_text[i]))
        key_indexes.append(alphabet_list.index(key[i]))

    # Substrract indexes and apply modulo 26
    plain_text_indexes = [
        (a - b) % 26 for a, b in zip(cipher_text_indexes, key_indexes)
    ]

    return "".join([alphabet_list[index] for index in plain_text_indexes])


if __name__ == "__main__":
    try:
        print("One Time Pad Encryption")
        print("Select an option: \n1. Encrypt\n2. Decrypt")
        option = int(input("Enter your choice: "))
        if option == 1:
            message = input("Enter the message: ").upper().replace(" ", "")
            print("Message: ", message)
            key = generateKey(len(message))
            print("Key: ", key)
            cipher_text = encrypt(message, key)
            print("Cipher text: ", cipher_text)
        elif option == 2:
            cipher_text = input("Enter the cipher text: ").replace(" ", "")
            key = input("Enter the key: ").replace(" ", "")
            plain_text = decrypt(cipher_text, key)
            print("Plain text: ", plain_text)
        else:
            raise ValueError
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print("An error occurred: ", e)
