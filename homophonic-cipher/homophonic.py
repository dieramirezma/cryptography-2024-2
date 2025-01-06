import random

layout = {
    "A": [9, 12, 33, 47, 53, 67, 78, 92],
    "B": [48, 81],
    "C": [13, 41, 62],
    "D": [1, 3, 45, 79],
    "E": [14, 16, 24, 44, 46, 55, 57, 64, 74, 82, 87, 98],
    "F": [10, 31],
    "G": [6, 25],
    "H": [23, 39, 50, 56, 65, 68],
    "I": [32, 70, 73, 83, 88, 93],
    "J": [15],
    "K": [4],
    "L": [26, 37, 51, 84],
    "M": [22, 27],
    "N": [18, 58, 59, 66, 71, 91],
    "O": [0, 5, 7, 54, 72, 90, 99],
    "P": [38, 95],
    "Q": [94],
    "R": [29, 35, 40, 42, 77, 80],
    "S": [11, 19, 36, 76, 86, 96],
    "T": [17, 20, 30, 43, 49, 69, 75, 85, 97],
    "U": [8, 61, 63],
    "V": [34],
    "W": [60, 89],
    "X": [28],
    "Y": [21, 52],
    "Z": [2],
}


def cipher(plain_text):
    cihper_text = ""
    for i in plain_text:
        cihper_text += str(random.choice(layout[i])) + " "
    return cihper_text


def decipher(cipher_text):
    plain_text = ""
    for i in cipher_text.strip().split(" "):
        for key, value in layout.items():
            if int(i) in value:
                plain_text += str(key)
                break
    return plain_text


if __name__ == "__main__":
    try:
        print("Homophonic Encryption")
        print("Select an option: \n1. Encrypt\n2. Decrypt")
        option = int(input("Enter your choice: "))
        if option == 1:
            message = input("Enter the message: ").upper().replace(' ', '')
            print("Message: ", message)
            cipher_text = cipher(message)
            print("Cipher text: ", cipher_text)
        elif option == 2:
            cipher_text = input("Enter the cipher text: ")
            plain_text = decipher(cipher_text)
            print("Plain text: ", plain_text)
        else:
            raise ValueError
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print("An error occurred: ", e)
