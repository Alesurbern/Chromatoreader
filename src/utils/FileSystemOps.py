import os
import platform
import pandas as pd

def clearScreen():
    so_name = platform.system()
    if so_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def change_directory():
    """Ask to the user for a new directory and 
        changes to the new one."""
    clearScreen()
    
    print("Current working directory.\n")
    print(">> ", os.getcwd())
    print()
    print("Introduce another directory or absolute path.\n")
    user_path = input("New directory: ")
    print()
    print("Current directory is:")

    try:
        os.chdir(user_path)
    except os.error:
        return "The path you passed is not valid.\n"
        
    print(os.getcwd())
    print()
    return "Directory changed.\n"

def load_excel_file():
    """Open the excel file written by the user."""

    clearScreen()

    print("Write the name of the Excel file.")
    excel_file_name = input("Excel file name: ")

    try:
        df = pd.read_excel(excel_file_name)
    except FileNotFoundError:
        return ("This file doesn't exist or there is an error with the name.\n", "", False)

    return ("", df, True)

def load_text_file():
    """Open the text file written by the user."""
    
    clearScreen()

    print("Write the name of the text file.")
    text_file_name = input("Text file name: ")

    try:
        #df = pd.read_csv(excel_file_name, sep="\t")
        df = pd.read_csv(text_file_name)
    except FileNotFoundError:
        return ("This file doesn't exist or there is an error with the name.\n", "", "", False)

    return ("", text_file_name, df, True)
