import customtkinter
import tkinter
import os
from PIL import Image
import shutil
from pathlib import Path

# Change the directory to the folder with the images
os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image Sorter - Github\Image-Sorter\images')

# List to store file numbers
file_number_array = []

# Supported image formats
supported_formats = ('.png', '.jpg', '.jpeg', '.tiff', '.raw')

# Convert alphabet to uppercase
def phrase_upper_check(phrase_alphabet_lower):
    return [s.upper() for s in phrase_alphabet_lower]

# Function to check and rename files
def rename_checker(phrase, phrase_uppercase, file_name):
    print(f'Checking file: {file_name}')
    if (file_name[0] in phrase) or (file_name[0] in phrase_uppercase):
        try:
            file_name_without_ext, file_ext = os.path.splitext(file_name)
            global image_format
            image_format = file_ext

            if '_' in file_name_without_ext:
                parts = file_name_without_ext.strip().split('_')
                if len(parts) == 2 and parts[1].isdigit():
                    clear_file, file_num = parts
                    file_names_reordered = f'{file_num}_{clear_file}{file_ext}'
                    print(f'Renaming {file_name} to {file_names_reordered}')
                    os.rename(file_name, file_names_reordered)
                    global file_number_array
                    file_number_array.append(int(file_num))
                    print(f'Appended {file_num} to file_number_array')
                else:
                    print(f'Skipping file {file_name} due to unexpected format: {parts}')
            else:
                print(f'Skipping file {file_name} due to missing underscore')
        except Exception as e:
            print(f'Error processing file {file_name}: {e}')
    else:
        file_name_without_ext, file_ext = os.path.splitext(file_name)
        parts = file_name_without_ext.strip().split('_')
        if len(parts) == 2:
            file_num, clear_file = parts
            file_names_reordered = f'{file_num}_{clear_file}{file_ext}'
            os.rename(file_name, file_names_reordered)
            file_number_array.append(int(file_num))
            print(f'Appended {file_num} to file_number_array')
            print('No need to change format')

# Initialize file renaming and number collection
alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphabet_uppercase = phrase_upper_check(alphabet)

for file_name in os.listdir():
    if os.path.splitext(file_name)[1].lower() in supported_formats:
        rename_checker(alphabet, alphabet_uppercase, file_name)

print("File numbers collected:", file_number_array)

if file_number_array:
    lowest_number = min(file_number_array)
    image_num = lowest_number
    print(f"The lowest file number is: {lowest_number}")
else:
    print("No file numbers collected.")

file_number_array = sorted(file_number_array)

# Function to display the next image in ascending order
def image_ascending():
    global image_num
    for num in file_number_array:
        if num > image_num:
            image_num = num
            break
    update_image()

# Function to display the previous image in descending order
def image_descending():
    global image_num
    for num in reversed(file_number_array):
        if num < image_num:
            image_num = num
            break
    update_image()

# Move file to "To_Be_Deleted" folder
def denied(event=None):
    global image_num, image_format
    deletion_folder = 'To_Be_Deleted'
    os.makedirs(deletion_folder, exist_ok=True)
    shutil.move(f'{image_num}_IMG{image_format}', deletion_folder)

    if image_num not in file_number_array:
        image_ascending()

    print('Image has been sent to To_Be_Deleted folder')
    update_image()

# Move file to "Approved_files" folder
def approved(event=None):
    global image_num, image_format
    approval_folder = 'Approved_files'
    os.makedirs(approval_folder, exist_ok=True)
    shutil.move(f'{image_num}_IMG{image_format}', approval_folder)

    if image_num not in file_number_array:
        image_ascending()

    print('Image has been sent to Approved_files folder')
    update_image()

# Display the previous image
def pre_image(event=None):
    global image_num
    print('Previous image')
    image_descending()
    update_image()

# Display the next image
def next_image(event=None):
    global image_num
    print('Next image')
    image_ascending()
    update_image()

# Update the image in the GUI
def update_image():
    global image_num, image_label, image_format
    for fmt in supported_formats:
        image_path = f'{image_num}_IMG{fmt}'
        if os.path.exists(image_path):
            image_format = fmt
            image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(image_width, image_height))
            image_label.configure(image=image)
            return
    print(f'Image {image_num}_IMG with supported formats {supported_formats} does not exist.')
    image_ascending()

# GUI setup
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry("1440x1280")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Image Sorter - version 1.0", font=("Roboto", 40))
label.pack(pady=12, padx=24)

image_width = 750
image_height = 450

# Initialize the first image loading
image_format = None
image_label = customtkinter.CTkLabel(root, image=None, text='')
image_label.place(x=590, y=120)

previous_Img_Btn = customtkinter.CTkButton(master=frame, text='<', corner_radius=30, font=('Roboto', 24), command=pre_image, height=32)
previous_Img_Btn.place(x=480, y=600)

denied_Btn = customtkinter.CTkButton(master=frame, text='Denied', corner_radius=18, font=('Roboto', 24), fg_color=('red', 'red'), command=denied, width=170, height=32)
denied_Btn.place(x=700, y=600)

approval_Btn = customtkinter.CTkButton(master=frame, text='Approved', corner_radius=18, font=('Roboto', 24), fg_color=('green', 'green'), command=approved, width=170, height=32)
approval_Btn.place(x=940, y=600)

next_Img_Btn = customtkinter.CTkButton(master=frame, text='>', corner_radius=30, font=('Roboto', 24), command=next_image, height=32)
next_Img_Btn.place(x=1190, y=600)

# Binding keys to the root window
root.bind('<f>', pre_image)
root.bind('<g>', denied)
root.bind('<h>', approved)
root.bind('<j>', next_image)

update_image()
root.mainloop()
