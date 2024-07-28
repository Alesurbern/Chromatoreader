import os
import pandas as pd

def change_directory():
    """Ask to the user for a new directory and 
        changes to the new one."""
    os.system("cls")
    
    print("Current working directory.")
    print(os.getcwd())
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

    os.system("cls")

    print("Write the name of the Excel file.")
    excel_file_name = input("Excel file name: ")

    try:
        df = pd.read_excel(excel_file_name)
        print(df)
    except FileNotFoundError:
        return "This file doesn't exist or there is an error with the name.\n"

    return ""

def load_text_file():
    """Open the text file written by the user."""

    os.system("cls")

    print("Write the name of the text file.")
    excel_file_name = input("Text file name: ")

    try:
        df = pd.read_csv(excel_file_name, sep="\t")
        print(df)
    except FileNotFoundError:
        return "This file doesn't exist or there is an error with the name.\n"

    return ""