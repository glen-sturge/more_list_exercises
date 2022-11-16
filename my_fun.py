def again():
    # Asks to continue.
    # Return True if 'Y', False if 'N'
    while True:
        go_again = input("Continue? (Y/N)   : ").upper()
        if go_again == "N":
            return False
        elif go_again == "Y":
            return True
        else:
            print("Error! Please Check Input.")


def blank(user_input: str):
    # Takes in str, Tests string, returns True if blank.
    if user_input == "":
        print("Error! No Input.")
        return True


# List making functions.
def make_list_str(minimum=0):
    # Asks for input from user.
    # Appends input as item in list of str.
    # Asks each time if user would like to continue.
    # Minimum Entries can be set.
    # Returns created list.
    print("Let's Make A New List Of Strings")
    print()
    str_list = []

    if minimum > 0:
        for i in range(0, minimum - 1):
            while True:
                new_entry = input("Supply Input        : ").strip()
                if not blank(new_entry):
                    break
            str_list.append(new_entry)

    while True:
        while True:
            new_entry = input("Supply Input        : ").strip()
            if not blank(new_entry):
                break
        str_list.append(new_entry)

        if not again():
            break
    return str_list


def make_list_int():
    # Asks for input from user.
    # Appends input as item in list of int (validated).
    # Asks each time if user would like to continue.
    # Returns created list.
    print("Make A New List Of Integers")
    print()
    int_list = []
    while True:
        while True:
            try:
                new_entry = int(input("Supply Input        : "))
            except ValueError:
                print("Error! Not A Number!")
            else:
                break
        int_list.append(new_entry)

        if not again():
            break
    return int_list


def make_list_float():
    # Asks for input from user.
    # Appends input as item in list of float (validated).
    # Asks each time if user would like to continue.
    # Returns created list.
    print("Make A New List Of Decimals")
    print()
    float_list = []
    while True:
        while True:
            try:
                new_entry = float(input("Supply Input        : "))
            except ValueError:
                print("Error! Not A Number!")
            else:
                break
        float_list.append(new_entry)

        if not again():
            break
    return float_list
