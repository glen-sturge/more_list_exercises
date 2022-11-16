def list_test(list_name: list):
    # Takes in a list.
    # Finds the number of strings in the list
    # where the string length is 2 or more and
    # the first and last character are same.
    # Returns the result.
    found = 0
    for i in range(len(list_name)):
        in_testing = list_name[i]
        if len(in_testing) >= 2 and in_testing[0] == in_testing[-1]:
            found += 1
    return found


def rmv_dupes(test_list):
    # Takes in list
    # creates new list without duplicate entries
    # returns new list.
    new_list = []
    for i in test_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def del_045(test_list: list):
    # receives list and returns list with 0th, 4th and 5th element removed.
    test_list.__delitem__(5)
    test_list.__delitem__(4)
    test_list.__delitem__(0)
    return test_list


def dif_sum_two_lists(list_1: list, list_2: list):
    # Takes in two lists of numbers.
    # Gets the sum of the items of each list.
    # Determine the difference of sums and return the value.
    sum_1 = sum(list_1)
    sum_2 = sum(list_2)
    difference = abs(sum_1 - sum_2)
    return difference


def element_frequency(sample_list: list):
    # Takes in a list.
    # Makes two lists.
    # One, a list without duplicates of original.
    # Two, a parallel list with the count of each occurrence.
    # Returns both lists.
    no_dupes_list = []
    count_list = []
    for i in sample_list:
        if i not in no_dupes_list:
            no_dupes_list.append(i)
            count_list.append(1)
        else:
            count_list[no_dupes_list.index(i)] += 1
    return no_dupes_list, count_list


def get_slice(sample_list: list):
    # Takes in a list.
    # Asks for start index and end index.
    # Returns that part of the list, inclusive of start and end.
    start = int(input("Enter Start Index : "))
    end = int(input("Enter End Index : ")) + 1
    return sample_list[start:end]


def concatenate_int(int_list: list):
    # Takes in a list of integers.
    # Converts each int item to str and concatenates into a single string.
    # Converts back to int and returns number.
    new_string = ""
    for i in int_list:
        new_string += str(i)
    number = int(new_string)
    return number


def first_char_search(this_list: list):
    # Takes in a list
    # Asks for input of char to compare to first char of each item of list.
    # Returns list of all positive results.
    results_list = []
    start_with = input("Enter Start Character : ")
    for i in this_list:
        if i[0] == start_with:
            results_list.append(i)
    return results_list


def rmv_consecutive_dupes(test_list: list):
    # Takes a list and creates new list without any consecutive duplicate items.
    # returns new list
    new_list = []
    count = 0
    for i in test_list:
        if count == 0:
            new_list.append(test_list[0])
            count += 1
        elif i != new_list[-1]:
            new_list.append(i)
    return new_list


def sort_fwd_bck(test_list: list):
    # takes a list and sorts ascending and descending into two new lists.
    # Returns both lists.
    forward_sort = sorted(test_list)
    backward_sort = sorted(test_list, reverse=True)
    return forward_sort, backward_sort
