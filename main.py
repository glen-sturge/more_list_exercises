# A program to encompass the 10 list exercises on the "More List Exercises" work sheet.
# Author: Glen Sturge       Date : 2022-11-14

# Imports
import app_fun as af


def main():
    while True:
        print()
        print("More List Exercises -- Main Menu")
        print("________________________________")
        print("        1. Exercise 1")
        print("        2. Exercise 2")
        print("        3. Exercise 3")
        print("        4. Exercise 4")
        print("        5. Exercise 5")
        print("        6. Exercise 6")
        print("        7. Exercise 7")
        print("        8. Exercise 8")
        print("        9. Exercise 9")
        print("       10. Exercise 10")
        print()
        print("       11. Quit")
        print("________________________________")
        print()

        while True:
            select = 0
            try:
                select = int(input("    Enter Selection : "))
            except ValueError:
                print("Error! That wasn't an integer.")
            if 1 <= select <= 11:
                print()
                print()
                break
            else:
                print("Selection out of range of options. Try again.")

        if select == 1:
            af.more_list_01()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 2:
            af.more_list_02()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 3:
            af.more_list_03()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 4:
            af.more_list_04()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 5:
            af.more_list_05()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 6:
            af.more_list_06()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 7:
            af.more_list_07()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 8:
            af.more_list_08()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 9:
            af.more_list_09()
            print()
            hold_screen = input("Press Enter To Continue...")
        elif select == 10:
            af.more_list_10()
            print()
            hold_screen = input("Press Enter To Continue...")
        else:
            print()
            print("Till Next Time!")
            break


if __name__ == '__main__':
    main()
