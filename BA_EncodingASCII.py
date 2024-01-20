
# @BA_X 20/01/2024


def to_text(dec_list):
    """
    Convert a list of decimal values to corresponding ASCII characters.

    Parameters:
        dec_list (list): List of decimal values.

    Returns:
        str: Concatenated ASCII characters.
    """
    text = ''

    for char_i in dec_list:
        if char_i <= 127:
            text += chr(char_i)
        else:
            print(f"{char_i} is not corresponding to an ASCII character. Try again")
            exit(-1)

    return text


def convert_binary_list(binary_list):
    """
    Convert a list of binary strings to a list of decimal values.

    Parameters:
        binary_list (list): List of binary strings.

    Returns:
        list: List of decimal values.
    """
    return [int(binary, 2) for binary in binary_list]


def convert_octal_list(octal_list):
    """
    Convert a list of octal strings to a list of decimal values.

    Parameters:
        octal_list (list): List of octal strings.

    Returns:
        list: List of decimal values.
    """
    return [int(octal, 8) for octal in octal_list]


def convert_decimal_list(dec_list):
    """
    Convert a list of decimal strings to a list of decimal values.

    Parameters:
        dec_list (list): List of decimal strings.

    Returns:
        list: List of decimal values.
    """
    return [int(dec) for dec in dec_list]


def convert_hex_list(hex_list):
    """
    Convert a list of hexadecimal strings to a list of decimal values.

    Parameters:
        hex_list (list): List of hexadecimal strings.

    Returns:
        list: List of decimal values.
    """
    return [int(hexadecimal, 16) for hexadecimal in hex_list]


def display_menu():
    """
    Display the main menu options.
    """
    print("Welcome! , BA_EncodingASCII")
    print("1. Binary List to Text")
    print("2. Octal List to Text")
    print("3. Decimal List to Text")
    print("4. Hexadecimal List to Text")
    print("5. The Manual")
    print("0. Exit")
    print("Please choose an option:", end='')


def display_manual():
    """
    Display the manual with accepted input formats.
    """
    print("***********************[Manual]*************************")

    print("Accepted input formats. Make sure to separate each character with a space.")
    print("For example:")
    print("1. Binary:\n'computer' -> 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010")
    print("2. Octal:\n'Hello' -> 110 145 154 154 157")
    print("3. Decimal:\n'World' -> 87 111 114 108 100")
    print("4. Hexadecimal:\n'Nice' -> 4E 69 63 65")

    print("********************************************************")


while True:
    display_menu()

    input_number = int(input())

    if input_number != 0 and input_number != 5:
        input_list = input("Enter the list : ")
        input_list = input_list.split()

        print("******************[Result]********************")

        if input_number == 1:
            print(to_text(convert_binary_list(input_list)))
        if input_number == 2:
            print(to_text(convert_octal_list(input_list)))
        if input_number == 3:
            print(to_text(convert_decimal_list(input_list)))
        if input_number == 4:
            print(to_text(convert_hex_list(input_list)))

        print("**********************************************")

    elif input_number == 5:
        display_manual()
    else:
        break
