import os
import pandas as pd
import Interface as iface
import FileSystemOps as io

#Function definitions

#Declared variables
main_loop = True
system_msg = ""
loaded_df = ""
is_df_loaded = False
result_df = ""

#Program start point

while(main_loop):
    os.system("cls")
    
    if is_df_loaded == False:
        iface.menu(system_msg)
        system_msg, loaded_df, is_df_loaded, main_loop = iface.decision_menu()
    
    else:
        iface.menu_loaded_df(system_msg, result_df)
        system_msg, result_df, is_df_loaded = iface.decision_menu_loaded_df(loaded_df)
    



"""
file_name = input("Name of the file: ")

df = pd.read_csv(file_name, sep="\t")
print(df)
"""
