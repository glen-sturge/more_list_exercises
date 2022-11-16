# Imports
import my_fun as mf
import list_fun as lf


def more_list_01():
    # Collects input from user and appends to list until user decides to stop.
    # Runs list_test, displays result.
    print()
    print("  More List Exercises -- Question 1.")
    print("......................................")
    print()
    print("Write a Python program to count the number of strings in the list where the string length is 2 or")
    print("more and the first and last character are same from a given list of strings.")
    print()
    print("Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2")
    print()

    this_list = mf.make_list_str()
    result = lf.list_test(this_list)

    print()
    print(f"Found : {result}")
    print()
    print()


def more_list_02():
    # Collects input from user and appends to list until user decides to stop.
    # Runs rmv_dupes, displays result
    print()
    print("  More List Exercises -- Question 2.")
    print("......................................")
    print()
    print("Write a Python program to remove duplicates from a list.")
    print()

    this_list = mf.make_list_str()

    result = lf.rmv_dupes(this_list)

    print()
    print(f"Your List With Duplicates Removed : {result}")
    print()
    print()


def more_list_03():
    # Collects input from user and appends to list until user decides to stop.
    # Runs del_045 on list and displays result
    print()
    print("  More List Exercises -- Question 3.")
    print("......................................")
    print()
    print("Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.")
    print()
    print("Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']")
    print("Expected Output : ['Green', 'White', 'Black']")
    print()

    this_list = mf.make_list_str(minimum=6)

    result = lf.del_045(this_list)

    print()
    print(f"Your List With The 0th, 4th And 5th Element's Removed : {result}")
    print()
    print()


def more_list_04():
    # Collects input from user and appends to list until user decides to stop.
    # Runs list_fun.dif_sum_two_lists on two lists of numbers and displays result
    print()
    print("  More List Exercises -- Question 4.")
    print("......................................")
    print()
    print("Write a Python program to get the difference of the sums between the two lists")
    print()

    this_list_1 = mf.make_list_int()
    this_list_2 = mf.make_list_int()
    result = lf.dif_sum_two_lists(this_list_1, this_list_2)

    print()
    print(f"The Difference Of The Sum Taken From Each List : {result}")
    print()
    print()


def more_list_05():
    # Collects input from user and appends to list until user decides to stop.
    # Runs list_fun.element_frequency on list then display results.
    print()
    print("  More List Exercises -- Question 5.")
    print("......................................")
    print()
    print("Write a Python program to get the frequency of the elements in a list.")
    print()

    this_list = mf.make_list_str()
    elements, count = lf.element_frequency(this_list)

    print()
    print("  Element     Count")
    print(".....................")
    for i in range(len(elements)):
        print(f" {elements[i]:>5}     |    {count[i]}")
    print(".....................")
    print()
    print()


def more_list_06():
    # Presents Sample list in table with indices noted.
    # Uses get_slice to ask user which part of the list is to be used.
    # Uses list_fun.element_frequency on the slice and displays results.

    # sample list and list with indices.
    index_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
    sample_list = ["A", "A", "B", "C", "C", "C", "D", "E", "E", "E", "F", "F", "G", "G", "H", "I", "I", "J"]

    print()
    print("  More List Exercises -- Question 6.")
    print("......................................")
    print()
    print("Write a Python program to count the number of elements in a list within a specified range.")
    print()

    print("  Index      Element")
    print(".....................")
    for i in range(len(index_list)):
        print(f"{index_list[i]:>5}     |     {sample_list[i]}")
    print(".....................")
    print()
    print("From The Table Above, Choose Start And End Indices.")

    this_list = lf.get_slice(sample_list)
    elements, count = lf.element_frequency(this_list)

    print()
    print(this_list)
    print()
    print("  Element     Count")
    print(".....................")
    for i in range(len(elements)):
        print(f" {elements[i]:>5}    |     {count[i]}")
    print(".....................")
    print()
    print()


def more_list_07():
    # Gets list of integers.
    # converts each to str and concatenates together
    # then converts back to int & displays result.

    print()
    print("  More List Exercises -- Question 7.")
    print("......................................")
    print()
    print("Write a Python program to convert a list of multiple integers into a single integer.")
    print()
    print("Sample list: [11, 33, 50], Expected Output: 113350")
    print()

    this_list = mf.make_list_int()

    new_number = lf.concatenate_int(this_list)

    print(f"The List Of Int         : {this_list}")
    print(f"The concatenated int is : {new_number}")
    print()
    print()


def more_list_08():
    # Provides sample list.
    # uses first_char_search
    # displays result.

    print()
    print("  More List Exercises -- Question 8.")
    print("......................................")
    print()
    print("Write a Python program to find the items that starts with specific input character from a given list.")
    print()

    sample_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

    print()
    print(f"This Is The Sample List : {sample_list}")

    result = lf.first_char_search(sample_list)

    print()
    print(f"Result Of Search : {result}")
    print()
    print()


def more_list_09():
    # Shows provided sample list of ints.
    # runs rmv_consecutive_dupes() on list
    # displays result

    sample_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    print()
    print("  More List Exercises -- Question 6.")
    print("......................................")
    print()
    print("Write a Python program to remove consecutive duplicates of a given list.")
    print()

    print(f"The Sample List : {sample_list}")

    result = lf.rmv_consecutive_dupes(sample_list)

    print()
    print(f"The result is : {result}")
    print()
    print()


def more_list_10():
    # Provides sample list.
    # Runs sort_fwd_bck().
    # Displays result.

    sample_list = [9, 4, 6, 7, 1, 3, 8, 10, 20, 15, 18, 13, 12]

    print()
    print("  More List Exercises -- Question 6.")
    print("......................................")
    print()
    print("Write a Python program that converts a list and sorts it in both ascending and descending order.")
    print()

    print(f"The Sample List : {sample_list}")
    print()
    ascending, descending = lf.sort_fwd_bck(sample_list)
    print(f"The Ascending Sorted List  : {ascending}")
    print(f"The Descending Sorted List : {descending}")
    print()
    print()
