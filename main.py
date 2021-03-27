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

import os                   # for file navigation
import docx                 # to read docX files
import click                # for creating the UI - may be unneccesary
from pathlib import Path    # for creating paths


def prompt_user() -> tuple:
    """prompt_user - prompts the user to enter an absolute filepath

    @param: None

    @return: A tuple containing [0] a string representing the folder path, and [1] a dictionary containing the actions to be performed
    @rtype : Tuple
    """
    pass


def traverse_directory(action_tuple: tuple) -> None:
    """traverse_directory - takes an input tuple containing a directory to traverse and actions to perform - reads all files from the directory and passes them to perform modification with the actions specified

    @param action_tuple: A tuple containing the directory to traverse and the actions to execute
    @type  action_tuple: tuple

    @return: None
    """

    directory = action_tuple[0]
    action_dict = action_tuple[1]
    actions = action_tuple[1].keys()

    for folderName, subfolders, filenames in os.walk(directory):

        # create an absolute file path for each file we need to edit
        for filename in filenames:
            file_path = Path(directory, filename)

            # for each action contained in the actions array, perform that action
            if "add_header" in actions:
                print("adding header to: " + filename)
                add_header(file_path, action_dict['add_header'])
            if "add_footer" in actions:
                print("adding footer to: " + filename)
                add_footer(file_path, action_dict['add_footer'])
            if "add_page_numbers" in actions:
                print("adding page numbers to: " + filename)
                add_page_numbers(file_path)


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


def add_footer(file: str, footer_text: str) -> None:
    """
    This function will add a footer to .docx/doc/txt file

    @param file: the file to add the footer to
    @Type file: string

    @Param footer_Text: the footer text to be added to each file
    @ type footer_text: string'''

    @return: None
    """

    # Check for  doc/docx and add footer to it
       if '.doc' in file or '.docx' in file:
            # Create footer for document object
            doc = docx.Document(file)
            # footer section
            footer_section = doc.sections[0]
            footer = footer_section.footer
            # footer text
            footer_text = footer.paragraphs[0]
            footer_text.text = footer_text
            doc.save(file)

        # Check for txt file and add footer to it

        # This will technically create new lines from paragraph text and just add to the end of the document
        # It will not create consistent page footers as there are not pages in a text document

        elif .'txt' in file:
            f_hand = open(file,'a+')
            f_hand.write(footer_text)
            f.hand.close()


        else:
            print('Error: You have to enter a text or doc/docx file')



def add_page_numbers(file: str) -> None:
    """add_page_numbers- adds page numbers to each page of a file

    @param file: the file to add the page numbers to
    @type  file: String
    """
    pass


if __name__ == "__main__":
    test_tuple = ('/home/noah/Developer/HackOR/HackOR/test_documents',
                  {"add_header": "this is a test"})
    traverse_directory(test_tuple)
