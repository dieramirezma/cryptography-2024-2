alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def getValues(type):
    message = input(f"Enter the {type} text: ").upper()

    k = input("Enter the key: ").upper().replace(" ", "")

    return (message, k)


def createMatrix(key):
    elements = key.replace("J", "I") + alphabet
    elements = list(dict.fromkeys(elements))
    matrix = [elements[i : i + 5] for i in range(0, len(elements), 5)]
    return matrix, elements


def replaceRepeated(string):
    string_list = list(string)
    for i in range(len(string)):
        if string_list[i] == string_list[i - 1] and string_list[i] != "X":
            string_list.insert(i, "X")
    if len(string_list) % 2 != 0:
        string_list.append("X")

    return "".join(string_list).replace(" ", "")


def printMatrix(matrix):
    for row in matrix:
        print(row)


def cipher(plaint_text, key):
    cipher_matrix, cipher_list = createMatrix(key)
    plain_text_list = replaceRepeated(plaint_text)

    plaint_text = ""
    cipher_text = ""

    for i in range(0, len(plain_text_list), 2):
        first_index = cipher_list.index(plain_text_list[i])
        plaint_text += f"{plain_text_list[i]}{plain_text_list[i + 1]} "
        second_index = cipher_list.index(plain_text_list[i + 1])

        row_1 = first_index // 5
        row_2 = second_index // 5
        col_1 = first_index % 5
        col_2 = second_index % 5

        if row_1 == row_2:
            cipher_text += f"{cipher_list[(first_index + 1) % (5 * (row_1 + 1))]}{cipher_list[(second_index + 1) % (5 * (row_1 + 1))]} "
        elif col_1 == col_2:
            cipher_text += f"{cipher_list[(first_index + 5) % 25]}{cipher_list[(second_index + 5) % 25]} "
        else:
            dif_row = row_1 - row_2
            if dif_row > 0:
                cipher_text += f"{cipher_list[(second_index + 5*dif_row) % 25]}{cipher_list[(first_index - 5*dif_row) % 25]} "
            else:
                cipher_text += f"{cipher_list[(second_index + 5*dif_row) % 25]}{cipher_list[(first_index - 5*dif_row) % 25]} "

    return plaint_text, cipher_text


def decipher(cipher_text, key):
    cipher_matrix, cipher_list = createMatrix(key)

    cipher_text_list = cipher_text.replace(" ", "")
    plain_text = ""
    cipher_text = ""

    for i in range(0, len(cipher_text_list), 2):
        first_index = cipher_list.index(cipher_text_list[i])
        second_index = cipher_list.index(cipher_text_list[i + 1])

        cipher_text += f"{cipher_text_list[i]}{cipher_text_list[i + 1]} "

        row_1 = first_index // 5
        row_2 = second_index // 5
        col_1 = first_index % 5
        col_2 = second_index % 5

        if row_1 == row_2:
            plain_text += f"{cipher_list[(first_index - 1) % (5 * (row_1 + 1))]}{cipher_list[(second_index - 1) % (5 * (row_1 + 1))]} "
        elif col_1 == col_2:
            plain_text += f"{cipher_list[(first_index - 5) % 25]}{cipher_list[(second_index - 5) % 25]} "
        else:
            dif_row = row_1 - row_2
            if dif_row > 0:
                plain_text += f"{cipher_list[(second_index + 5*dif_row) % 25]}{cipher_list[(first_index - 5*dif_row) % 25]} "
            else:
                plain_text += f"{cipher_list[(second_index + 5*dif_row) % 25]}{cipher_list[(first_index - 5*dif_row) % 25]} "

    return cipher_text, plain_text


if __name__ == "__main__":
    try:
        print("Playfair Encryption")
        print("Select an option: \n1. Encrypt\n2. Decrypt")
        option = int(input("Enter your choice: "))
        if option == 1:
            plain_text, key = getValues("plain")
            plain_text_divide, cipher_text = cipher(plain_text, key)

            print("Plain text: ", plain_text_divide)
            print("Cipher text: ", cipher_text)
        elif option == 2:
            cipher_text, key = getValues("cipher")
            cipher_text_divide, plain_text = decipher(cipher_text, key)

            print("Cipher text: ", cipher_text_divide)
            print("Plain text: ", plain_text)
        else:
            raise ValueError
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print("An error occurred: ", e)
