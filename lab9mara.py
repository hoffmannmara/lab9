# mara hoffmann

def encode(password):
    encoded_pass = ''
    for i in password:
        encoded_num = str(int(i) + 3)
        encoded_pass += encoded_num
    return encoded_pass


def main():
    while True:
        print("Menu\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit\n")

        option = int(input("Please enter an option: "))
        password = (input("Please enter your password to encode: "))

        if option == 1:
            print("Your password has been encoded and stored!")
        if option == 2:
            encoded_password = encode(password)
            decoded_password = decode(password)
            print(f"The encoded password is {encoded_password} and the original password is {decoded_password}")
        if option == 3:
            exit()







if __name__ == '__main__':
    main()
