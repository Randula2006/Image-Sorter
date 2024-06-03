
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



file_number_array = []



def phrase_upper_check(phrase_alphebet_lower):
    return [s.upper() for s in phrase_alphebet_lower]



def rename_checker(phrase, phrase_uppercase, file_name):
    
    print(f'Checking file: {file_name}')  # Debugging statement
    
    # evaluating if the file has the alphebet lower or uppercase in the filename 
    if (file_name[0] in phrase) or (file_name[0] in phrase_uppercase):
        
        try:
            # Renaming checker if the value starts with a letter
            file_name_without_ext, file_ext = os.path.splitext(file_name)
            # Ensure the filename contains an underscore and can be split into two parts
            
            if '_' in file_name_without_ext:
                # Strip and split the file name
                parts = file_name_without_ext.strip().split('_')
                
                # checking the length of the file 
                if len(parts) == 2 and parts[1].isdigit():
                    
                    clear_file, file_num = parts
                    # Reorder the file name
                    file_names_reordered = f'{file_num}_{clear_file}{file_ext}'
                    # Printing the renamed file 
                    print(f'Renaming {file_name} to {file_names_reordered}')
                    # Rename the file
                    os.rename(file_name, file_names_reordered)
                    # Append the file number to the global array
                    
                    
                    global file_number_array
                    file_number_array.append(int(file_num))  # Ensure file_num is stored as an integer
                    print(f'Appended {file_num} to file_number_array')  # Debugging statement
                    
                else:
                    print(f'Skipping file {file_name} due to unexpected format: {parts}')
            else:
                print(f'Skipping file {file_name} due to missing underscore')
                
                
        except Exception as e:
            print(f'Error processing file {file_name}: {e}')  # Debugging statement
    else:
         global file_number_array
         file_number_array.append(int(file_num))  # Ensure file_num is stored as an integer
         print(f'Appended {file_num} to file_number_array')  # Debugging statement
         
         print('No need to change format') 
        

# Change to the directory containing the files
os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image Sorter - Github\Image-Sorter\images')
print(os.getcwd())


alphebet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_uppercase = phrase_upper_check(alphebet)



for file_name in os.listdir():
    rename_checker(alphebet, alphabet_uppercase, file_name)

print("File numbers collected:", file_number_array)


# Find and print the lowest number in the file_number_array
if file_number_array:
    lowest_number = min(file_number_array)
    print(f"The lowest file number is: {lowest_number}")
else:
    print("No file numbers collected.")


##################################################################
# posible errors

# if the file is not chcked the value is not sent to the array of integers