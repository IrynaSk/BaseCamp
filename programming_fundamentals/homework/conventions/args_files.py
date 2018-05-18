#!/usr/bin/env python
"""
This module contains tasks related to arguments & parameters, files in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"
import re
FILENAME = 'awesome_data.txt'
lines = [
    "Two assure edward whence the was.",
    "Who worthy yet ten boy denote wonder.",
    "Weeks views her sight old tears sorry.",
    "Additions can suspected its concealed put furnished.",
    "Met the why particular devonshire decisively considered partiality.",
    "Certain it waiting no entered is.",
    "Passed her indeed uneasy shy polite appear denied.",
    "Oh less girl no walk.",
    "At he spot with five of view."
]

USER_INFO = {
    "name": "Pavlo",
    "surname": "Ivanchyshyn",
    "age": 28,
    "city": "Lviv"
}


def find_sum(*args):
    """
    Implement this function!
    This function should sum of numbers for different amount of parameters.

    It should be similar to built-in `sum` function.
    DON'T use `sum` function here.

    Returns:
        int - sum of numbers.

    Examples:
        find_sum(1, 2, 3)  # Returns 6.
        find_sum(1)  # Returns 1.
        find_sum([1, 3])  # Returns 4.
        find_sum(1, 2, 3, 4, 5, 6)  # Returns 21.
        etc.
    """
    # ADD YOUR CODE HERE.
    sum = 0
    for arg in args:
        if type(arg) == list:
            for el in arg:
                sum += el
        else:
            sum += arg
    return sum


def write_to_file(filename, data):
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.

    with open(filename, 'w') as file:
        for element in data:
            file.write(element + '\n')
    return


def read_file(filename):
    """
    Implement this function!
    This function should read all the lines from the file with `filename`.

    Args:
        filename (str) - name of file for writing.

    Returns:
        list - list of lines from the file.
    """
    # ADD YOUR CODE HERE.

    with open(filename, 'r') as file:
        text = file.readlines()
        return text


def append_to_file(filename, data):
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    with open(filename, 'a') as file:
        for line in data:
            file.write(line + "\n")
    return


def write_user_info(filename, data):
    """
    Using function `write_to_file` do the following:
    - Create file with a `filename` name.
    - Write user's information from `data` into file with `filename` in the following format:

    Hi there!
    My name is <name> <surname>.
    I am <age> years old.
    I live in <city>.

    Where values in `<>` mean the keys from `data` object.

    Args:
        filename (str) - name of file for writing.
        data (dict) - personal user's information.
    """
    # ADD YOUR CODE HERE.
    data = (
        "Hi there!",
        "My name is {} {}.".format(data['name'], data['surname']),
        "I am {} years old.".format(data['age']),
        "I live in {}.".format(USER_INFO['city']))
    write_to_file(filename, data)
    return


def get_user_info(filename):
    """
        Using file created by `write_user_info` create a reader. It should be able to read the following format:

        Hi there!
        My name is <name> <surname>.
        I am <age> years old.
        I live in <city>.

        Where values in `<>` mean the keys from `data` object.

        Args:
            filename (str) - name of file for writing.

        Returns
            dict - personal user's information.

        Example:
            get_user_info(FILENAME)  # Returns {"name": "Pavlo", "surname": "Ivanchyshyn", "age": 28, "city": "Lviv"}
    """

    data = read_file(filename)

    def search_value(patterns_start, pattern_end, data):
        match = re.search(patterns_start, data)
        if match:
            pos_start_value = match.end()
            match2 = re.search(pattern_end, data)
            if match2:
                pos_end_value = match2.start()
                value = data[pos_start_value:pos_end_value]
                return value

    name = search_value(r"(\s[a-z][a-z]\s)", r"(\s[A-Z]([a-z]+)\.)", data[1])
    surname = search_value(r"(\s[A-Z]([a-z]+)\s)", r"\.\n", data[1])
    age = search_value(r"(\s[a-z][a-z]\s)", r" years", data[2])
    city = search_value(r"(\s[a-z][a-z]\s)", r"\.", data[3])
    dict = {}
    dict['name'] = name
    dict['surname'] = surname
    dict['age'] = age
    dict['city'] = city
    print(dict)
    return dict


# get_user_info(FILENAME)

