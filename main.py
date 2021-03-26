#################################################################################################
#                                                                                               #
#       Batch Editor (insert fun name here) - a Python Program Written for HackOR 2021          #
#       Written by:                                                                             #
#           Sophia L                                                                            #
#           Ryan R.                                                                             #
#           Noah S.                                                                             #
#           Rain_Bow?                                                                           #
#                                                                                               #
#################################################################################################

# necessary libraries
import os           # for file navigation
import docx         # for manipulating .docX files
import click        # for creating the UI


def prompt_user() -> tuple:
    """promt_user - prompts the user to enter an absolute filepath

    @param None:  Description
    @type  None:  Type

    @return: a string representing the absolute filepath
    @rtype : String
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


if __name__ == "__main__":
    pass
