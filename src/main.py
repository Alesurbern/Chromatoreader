import os
import pandas as pd
import utils.Interface as iface
import utils.FileSystemOps as io

#Function definitions

#Declared variables
main_loop = True
system_msg = ""
name_loaded_df = ""
loaded_df = ""
is_df_loaded = False
result_df = ""

#Program start point

while(main_loop):
    io.clearScreen()
 
    if is_df_loaded == False:
        iface.menu(system_msg)
        system_msg, name_loaded_df, loaded_df, is_df_loaded, main_loop = iface.decision_menu()
    
    else:
        iface.menu_loaded_df(system_msg, result_df, name_loaded_df)
        system_msg, result_df, is_df_loaded = iface.decision_menu_loaded_df(loaded_df)
    
