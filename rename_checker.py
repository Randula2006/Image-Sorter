
import os
import re
import customtkinter
import tkinter
import PIL as Image
from pathlib import Path
import shutil


# image_num = 515 #temp value

# def denied(event = None):
#     event = 1
#     if event == 1 :
#         image_num += 1
#     else:
#         print("error in the program: error 201")
    


# denied()


# target_folder = r"file_path" + '\\'
# source_folder = r"to the folder that we have to move" + "\\"




# code

# os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image sorter\images')

# Path("To_Be_Deleted").mkdir(exist_ok=True)
# # this will create a new data directory

# for file in os.listdir():
#      if file =='Renaming of Multiple Files.mp4' or file == 'To_Be_Deleted':
#          continue
#      shutil.move(file , 'To_Be_Deleted')
     
# code 


     
#  the data can either have a file name or a whole directory name
# by using move2 we can save all the meta data in the files 

import os

from numpy import append

file_number_array = []

def phrase_upper_check(phrase_alphebet_lower):
    return [s.upper() for s in phrase_alphebet_lower]


def rename_checker(phrase, phrase_uppercase , file_name):
    # for phrase, phrase_uppercase in zip(alphebet, alphabet_uppercase):
        
        if (file_name[0] in phrase) or (file_name[0] in phrase_uppercase):
             # renaming checker if the value starts with a letter 
             file_name_without_ext, file_ext = os.path.splitext(file_name)
        
             # Strip and split the file name
             clear_file, file_num = file_name_without_ext.strip().split('_')
        
             # Reorder the file name
             file_names_reordered = f'{file_num}_{clear_file}{file_ext}'
             # printing the renamed file 
             print(f'Renaming {file_name} to {file_names_reordered}')
        
             # Rename the file
             os.rename(file_name, file_names_reordered)
             
            #  appending the value file_number to file_number_array list 
             global file_number_array
             file_number_array.append(file_num)
             
             
        else:
                print('No need to change format') 
     

os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image sorter\images')

print(os.getcwd())



alphebet = ['a', 'b' ,'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = phrase_upper_check(alphebet)
# print(alphabet_uppercase)

for file_name in os.listdir():
    
    rename_checker(alphebet, alphabet_uppercase , file_name)
    
