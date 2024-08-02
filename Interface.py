import FileSystemOps as io

def banner():
    """Print the title of the program"""

    print("")
    print("CHROMATOGRAM READER")
    print("===================")
    print()
    
def menu(sysmsg):
    """Print the first menu and the message 
        to the user"""

    banner()

    if sysmsg != "":
        print("System message: " + sysmsg)
        
    print("1. Load an excel file")
    print("2. Load a csv or text file")
    print("3. Change directory.")
    print("4. Exit.")
    print()

def decision_menu():
    """Control flow for the menu"""

    system_msg = ""
    name_loaded_df = ""
    loaded_df = ""
    is_df_loaded = False
    main_loop = True

    user_menu_input = input("Your selection: ")

    if(user_menu_input == "1"):
        print("Loading an excel file.\n")
        system_msg, loaded_df, is_df_loaded = io.load_excel_file()

    elif (user_menu_input == "2"):
        print("Loading a csv or text file.\n")
        system_msg, name_loaded_df, loaded_df, is_df_loaded = io.load_text_file()

    elif (user_menu_input == "3"):
        print("Changing directory.\n")
        system_msg = io.change_directory()

    elif (user_menu_input == "4"):
        print("Closing the program.\n")
        main_loop = False

    else:
        system_msg = "Error. Input not recognized.\n"

    return (system_msg, name_loaded_df, loaded_df, is_df_loaded, main_loop)

def menu_loaded_df(sysmsg, result_df, name_df):
    """Print the menu when the df is loaded"""

    banner()

    if sysmsg != "":
        print("System message: " + sysmsg)
        
    print("File: ", name_df)
    print("")
    print(result_df)
    print("")

    print("----------------------------------------")
    print("1. Print the data frame.")
    print("2. Print first rows of the data frame.")
    print("3. Print last rows of the data frame.")
    print("4. Print the name of the columns.")
    print("5. Go back.")
    print()

def decision_menu_loaded_df(df):
    """Control flow for the menu"""

    system_msg = ""
    result_df = ""
    is_df_loaded = True

    user_menu_input = input("Your selection: ")

    if(user_menu_input == "1"):
        print("Print the data frame.\n")
        result_df = df

    elif (user_menu_input == "2"):
        print("Print first rows of the data frame.\n")
        result_df = df.head()

    elif (user_menu_input == "3"):
        print("Print last rows of the data frame.\n")
        result_df = df.tail()

    elif (user_menu_input == "4"):
        print("Print the name of the columns.\n")
        result_df = df.columns

    elif (user_menu_input == "5"):
        print("Go back.\n")
        is_df_loaded = False

    else:
        system_msg = "Error. Input not recognized.\n"

    return (system_msg, result_df, is_df_loaded)