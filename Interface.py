def banner():
    """Print the title of the program"""

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
