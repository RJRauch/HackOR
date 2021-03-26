#################################################################################################
#                                                                                               #
#       Batch Editor (insert fun name here) - a Python Program Written for HackOR 2021          #
#       Written by:                                                                             #
#           Sophia L                                                                            #
#           Ryan R.                                                                             #
#           Noah S.                                                                             #
#                                                                                               #
#################################################################################################

# necessary libraries

import os           # for file navigation
import docx         # to read docX files
import click        # for creating the UI - may be unneccesary


def prompt_user() -> tuple:
    """prompt_user - prompts the user to enter an absolute filepath

    @param: None

    @return: A tuple containing (a string representing the file path, [a list of the actions to be undertaken])
    @rtype : Tuple
    """
    pass


def traverse_directory(action_tuple: tuple) -> None:
    """traverse_directory - takes an input tuple containing a directory to traverse and actions to perform - reads all files from the directory and passes them to perform modification with the actions specified

    @param action_tuple: A tuple containing the directory to traverse and the actions to execute
    @type  action_tuple: tuple

    @return: None
    """
    pass


def perform_modification(filepath: str, mod_function) -> None:
    """reads in a filepath and a function to modify the files in that path. Performs the function on each file found.

    @param filepath: The filepath to search for document files
    @type  filepath: String

    @param mod_function: The function to be performed on each
    @type  mod_function: String

    @return: None
    """
    pass


def add_header(file: str, header_text: str) -> None:
    """add_header - adds header text to a file

    @param file: the file to add the header to
    @type  file: String

    @param header_text: The header text to be added to each file
    @type  header_text: String

    @return: None
    """
    pass


def add_footer(file: str, footer_text: str) -> None:
    """add_footer - adds footer text to a file

    @param file: the file to add the footer to
    @type  file: String

    @param footer_text: The footer text to be added to each file
    @type  footer_text: String

    @return: None
    """
    pass


def add_page_numbers(file: str) -> None:
    """add_page_numbers- adds page numbers to each page of a file

    @param file: the file to add the page numbers to
    @type  file: String
    """
    pass


if __name__ == "__main__":
    print("Hello, World!")
