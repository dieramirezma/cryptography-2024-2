A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getValues(type):
  message = input(f"Enter the {type} text: ").upper().replace(" ", "")

  m = int(input("\nEnter the length of substrings: "))
  k = int(input("Enter the number of permutations: "))

  return (message, m, k)

def divideString(string, m):
  return [string[i:i+m] for i in range(0,len(string), m)]

def replaceCharacter(M, k):
  n = len(M)

  M_list = list(M)

  for i in range(n):
    A_index = A.index(M_list[i])
    M_list[i] = A[(A_index + k) % 26]

  return ''.join(M_list)

def encrypt(M, k):
  cipher_text = []

  for string in M:
    cipher_string = replaceCharacter(string, k)
    cipher_text.append(cipher_string)

  return ' '.join(cipher_text)

def decrypt(M, k):
  plain_text = []

  for string in M:
    plain_string = replaceCharacter(string, -k)
    plain_text.append(plain_string)

  return ' '.join(plain_text)

if __name__ == '__main__':
  try:
    print("Caesar's Encryption")
    print("Select an option: \n1. Encrypt\n2. Decrypt")
    option = int(input("Enter your choice: "))
    if option == 1:
      plain_text, m, k = getValues('plain')

      M = divideString(plain_text, m)
      cipher_text = encrypt(M, k)

      print("\nCipher text: ", cipher_text)
    elif option == 2:
      cipher_text, m, k = getValues('cipher')

      M = divideString(cipher_text, m)

      plain_text = decrypt(M, k)
      print("\nPlain text: ", plain_text)
    else:
      raise ValueError
  except ValueError:
    print("Invalid input.")
  except Exception as e:
    print("An error occurred: ", e)
