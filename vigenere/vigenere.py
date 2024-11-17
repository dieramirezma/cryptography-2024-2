alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def getValues(type):
  message = input(f"Enter the {type} text: ").upper().replace(" ", "")

  k = input("Enter the key: ").upper().replace(" ", "")

  m = int(input("\nEnter the length of substrings: "))

  return (message, k, m)

def createMatrix():
  matrix = []

  for i in range(len(alphabet)):
    matrix.append(alphabet[i:] + alphabet[:i])

  return matrix

def printMatrix(matrix):
  for row in matrix:
    print(row)

def divideString(string, m):
  return [string[i:i+m] for i in range(0,len(string), m)]

def generateKeyList(key, n):
  key_list = ''

  for i in range(n):
    key_list += key[i % len(key)]

  return key_list

def encrypt(plain_text, matrix, key):
  cipher_text = ''

  for plain_str, key_str in zip(plain_text, key):
    division = ""
    for index in range(5):
      i = alphabet.index(key_str[index])
      j = alphabet.index(plain_str[index])
      division += matrix[i][j]
    cipher_text += division + " "

  return cipher_text

def decrypt(cipher_text, matrix, key):
  plain_text = ''

  for cipher_str, key_str in zip(cipher_text, key):
    division = ""
    for index in range(5):
      i = alphabet.index(key_str[index])
      j = matrix[i].index(cipher_str[index])
      division += alphabet[j]
    plain_text += division + " "

  return plain_text

if __name__ == '__main__':
  try:
    print("Vigenere's Encryption")
    print("Select an option: \n1. Encrypt\n2. Decrypt")
    option = int(input("Enter your choice: "))
    matrix = createMatrix()
    if option == 1:
      plain_text, k, m = getValues('plain')

      M = divideString(plain_text, m)

      key_extended = generateKeyList(k, len(plain_text))
      key = divideString(key_extended, m)

      cipher_text = encrypt(M, matrix, key)

      print()
      print(" ".join(key))
      print(" ".join(M))

      print("\nCipher text: ", cipher_text)
    elif option == 2:
      cipher_text, k, m = getValues('cipher')

      M = divideString(cipher_text, m)

      key_extended = generateKeyList(k, len(cipher_text))
      key = divideString(key_extended, m)

      plain_text = decrypt(M, matrix, key)

      print()

      print(" ".join(key))
      print(" ".join(M))

      print("\nPlain text: ", plain_text)
    else:
      raise ValueError
  except ValueError:
    print("Invalid input.")
  except Exception as e:
    print("An error occurred: ", e)

