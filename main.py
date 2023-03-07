def password_encoder(decoded_password):
    decoded_password_list = list(decoded_password)
    encoded_password = ''
    for char in decoded_password_list:
        char = int(char)
        if 7 <= char <= 9:
            char -= 7
            char = str(char)
            encoded_password += char
        elif 0 <= char <= 6:
            char += 3
            char = str(char)
            encoded_password += char
    return encoded_password


def print_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


if __name__ == '__main__':
    # take in the 8-digit password
    password_input = ''
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        # password_input = ''
        if option == 1:
            # 1. Encode
            password_input = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            password_encoder(password_input)
        elif option == 2:
            # 2. Decode
            encoded_password = password_encoder(password_input)
            print(f"The encoded password is {encoded_password}, and the original password is {password_input}.\n")
        elif option == 3:
            # 3. Quit
            break
