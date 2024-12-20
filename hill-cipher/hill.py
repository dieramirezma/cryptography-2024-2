import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def getValues(type):
    print("Input the key matrix: ")
    key = getMatrix()
    message = input(f"Enter the {type} text: ").upper().replace(" ", "")

    return (message, key)


def getMatrixDeterminant(m: list) -> int:
    return int(np.linalg.det(m))


def calculateMatrixInverse(m: list) -> list:
    det = getMatrixDeterminant(m)
    inv = np.linalg.inv(m)
    inv = (inv * det) % 26
    inv = np.round(inv).astype(int)
    return inv


def checkMatrix(m: list) -> bool:
    det = getMatrixDeterminant(m)
    if det == 0:
        return False
    coprime = gcd(det, 26)
    if coprime != 1:
        return False
    return True


def gcd(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def getMatrix():
    n = int(input("Enter the size of the matrix: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Input row {i} space separated: ").split()))
        matrix.append(row)
    return np.array(matrix)


def hill_cipher(plain_text, key):
    n = len(key)
    cipher_text = ""
    if len(plain_text) % n != 0:
        plain_text += "X" * (n - len(plain_text) % n)
    plain_text = np.array([alphabet.index(i) for i in plain_text])

    for i in range(0, len(plain_text), n):
        x = plain_text[i : i + n]
        y = np.dot(x, key) % 26
        cipher_text += "".join([alphabet[i] for i in y])

    return cipher_text


def hill_decipher(cipher_text, key):
    n = len(key)
    inverse = calculateMatrixInverse(key)
    plain_text = ""
    if len(cipher_text) % n != 0:
        cipher_text += "X" * (n - len(cipher_text) % n)
    cipher_text = np.array([alphabet.index(i) for i in cipher_text])

    for i in range(0, len(cipher_text), n):
        x = cipher_text[i : i + n]
        y = np.dot(x, inverse) % 26
        plain_text += "".join([alphabet[i] for i in y])

    return plain_text


if __name__ == "__main__":
    try:
        print("Hill's Encryption")
        print("Select an option: \n1. Encrypt\n2. Decrypt")
        option = int(input("Enter your choice: "))
        if option == 1:
            plain_text, key = getValues("plain")

            if not checkMatrix(key):
                print("Matrix is not invertible.")
                exit()

            cipher_text = hill_cipher(plain_text, key)
            print(f"Plain text: {cipher_text}")
        elif option == 2:
            cipher_text, key = getValues("cipher")

            if not checkMatrix(key):
                print("Matrix is not invertible.")
                exit()

            plain_text = hill_decipher(cipher_text, key)
            print(f"Plain text: {plain_text}")
        else:
            raise ValueError
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print("An error occurred: ", e)
