import os
import pandas as pd
import Interface as iface
import FileSystemOps as io

#Function definitions

#Declared variables
main_loop = True
system_msg = ""
loaded_df = ""

#Program start point

while(main_loop):
    os.system("cls")
    
    iface.menu(system_msg)
    
    user_menu_input = input("Your selection: ")

    if(user_menu_input == "1"):
        print("Loading an excel file.\n")
        system_msg, loaded_df = io.load_excel_file()

    elif (user_menu_input == "2"):
        print("Loading a csv or text file.\n")
        system_msg, loaded_df = io.load_text_file()

    elif (user_menu_input == "3"):
        print("Changing directory.\n")
        system_msg = io.change_directory()

    elif (user_menu_input == "4"):
        print("Closing the program.\n")
        main_loop = False

    else:
        system_msg = "Error. Input not recognized.\n"



"""
file_name = input("Name of the file: ")

df = pd.read_csv(file_name, sep="\t")
print(df)
"""
