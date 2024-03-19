# Valerie Samuels 


# print out a menu
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


# allow the user to choose a menu option
def menu_choice():
    print_menu()
    while True:
        choice = input("Please enter an option: ")

        if int(choice) == 1:
            return 1

        elif int(choice) == 2:
            return 2

        elif int(choice) == 3:
            return 3

        else:
            continue


# create a function that will encode the user's password
def encode(user_original_password):
    encoded_password = ""

    for num in user_original_password:
        # for each number in the password we will add 3 to it
        encoded_num = int(num) + 3

        # if the resulting number is greater than 9 we have to subtract 10
        if encoded_num > 9:
            encoded_num -= 10

        # add the encoded digits in the correct order
        encoded_password += str(encoded_num)

    return encoded_password


# this is where my partner will write a decoding function
def decode(user_encoded_password):
    user_encoded_password = list(str(user_encoded_password))
    number = int()
    for i in range(0, len(user_encoded_password)):
        number = int(user_encoded_password[i])
        number -= 3
        if number < 0:
            number += 10
        user_encoded_password[i] = str(number)
    user_encoded_password = ''.join(user_encoded_password)
    return user_encoded_password


# write the program logic
def main():
    while True:
        # ask the user for which menu option
        user_choice = menu_choice()

        # user chooses to exit
        if user_choice == 3:
            break

        # user chooses to encode a password
        elif user_choice == 1:
            user_original_password = input(f"Please enter your password to encode: ")
            user_encoded_password = encode(user_original_password)
            print("Your password has been encoded and stored!")
            continue

        # the user will choose to decode the encoded password that they input earlier
        elif user_choice == 2:
            user_decoded_password = decode(user_encoded_password)
            print(f"The encoded password is {user_encoded_password}, and the original password is {user_decoded_password}.")
            continue


# run the code
if __name__ == "__main__":
    main()