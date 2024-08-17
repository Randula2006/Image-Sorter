import customtkinter
import tkinter
import os
from PIL import Image
import shutil
from pathlib import Path
import rawpy
import imageio

# changing the directory to the folder with the images
os.chdir(r'D:\Programming\python\Rebooting\projects\Image Sorter - Github\Image-Sorter\images')

file_number_array = []

def phrase_upper_check(phrase_alphebet_lower):
    return [s.upper() for s in phrase_alphebet_lower]

def rename_checker(phrase, phrase_uppercase, file_name):
    print(f'Checking file: {file_name}')
    if (file_name[0] in phrase) or (file_name[0] in phrase_uppercase):
        try:
            file_name_without_ext, file_ext = os.path.splitext(file_name)
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
        else:
            print(f'Skipping file {file_name} due to unexpected format: {parts}')
        print('No need to change format')

# Change to the directory containing the files
os.chdir(r'D:\Programming\python\Rebooting\projects\Image Sorter - Github\Image-Sorter\images')
print(os.getcwd())

alphebet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uppercase = phrase_upper_check(alphebet)

for file_name in os.listdir():
    rename_checker(alphebet, alphabet_uppercase, file_name)

print("File numbers collected:", file_number_array)

# Find and print the lowest number in the file_number_array
if file_number_array:
    lowest_number = min(file_number_array)
    image_num = lowest_number
    print(f"The lowest file number is: {lowest_number}")
else:
    print("No file numbers collected.")

file_number_array = sorted(file_number_array)

##################################################################
# Function to convert CR3 to JPG
def convert_cr3_to_jpg(cr3_file):
    """Convert CR3 file to JPG and return the image object."""
    try:
        with rawpy.imread(cr3_file) as raw:
            rgb_image = raw.postprocess()
        jpg_file = cr3_file.replace('.CR3', '.jpg')
        imageio.imsave(jpg_file, rgb_image)
        return jpg_file
    except Exception as e:
        print(f'Error converting {cr3_file}: {e}')
        return None

# Functions for navigating images
def image_ascending():
    global image_num
    for num in file_number_array:
        if num > image_num:
            image_num = num
            break
        elif num == image_num:
            print('Highest image has been displayed')
        else:
            print('No images above this')
    update_image()

def image_descending():
    global image_num
    for num in reversed(file_number_array):
        if num < image_num:
            image_num = num
            break
        elif num == image_num:
            print('Lowest image has been displayed')
        else:
            print('No images below this')
    update_image()

# Functions for GUI button actions
def denied(event=None):
    global image_num
    deletion_folder = 'To_Be_Deleted'
    os.makedirs(deletion_folder, exist_ok=True)
    shutil.move(f'{image_num}_IMG.JPG', deletion_folder)
    if image_num not in file_number_array:
        image_ascending()
    print('Image has been sent to To_Be_Deleted folder')
    update_image()

def approved(event=None):
    global image_num
    approval_folder = 'Approved_files'
    os.makedirs(approval_folder, exist_ok=True)
    shutil.move(f'{image_num}_IMG.JPG', approval_folder)
    if image_num not in file_number_array:
        image_ascending()
    print('Image has been sent to Approved_files folder')
    update_image()

def pre_image(event=None):
    global image_num
    print('Previous image')
    image_descending()
    update_image()

def next_image(event=None):
    global image_num
    print('Next image')
    image_ascending()
    update_image()

# Function to update the image in the GUI
def update_image():
    global image_num, image_label
    
    image_path = '{}_IMG.JPG'.format(image_num)
    cr3_image_path = '{}_IMG.CR3'.format(image_num)
    
    if os.path.exists(image_path):
        image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(image_width, image_height))
        image_label.configure(image=image)
    elif os.path.exists(cr3_image_path):
        jpg_path = convert_cr3_to_jpg(cr3_image_path)
        if jpg_path:
            image = customtkinter.CTkImage(light_image=Image.open(jpg_path), size=(image_width, image_height))
            image_label.configure(image=image)
        else:
            print(f'Failed to display image {cr3_image_path}')
    else:
        print(f'Image {image_path} or {cr3_image_path} does not exist.')
        image_ascending()

# GUi area 

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
# general dimensions 
root.geometry("1440x1280")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame , text="Image Sorter - version 1.0", font=("Roboto", 40))
label.pack(pady=12, padx=24)

# Adding the images for slideshow

# image size height and width
image_width = int(750)
image_height = int(450)

# Initialize the image (empty)
image_path = '{}_IMG.JPG'.format(image_num)
if os.path.exists(image_path):
    image  = customtkinter.CTkImage(light_image=Image.open(image_path), size=(image_width, image_height))
else:
    image = None

# Label creation for the images
image_label = customtkinter.CTkLabel(root, image=image, text='')
image_label.place(x=590, y=120)

previous_Img_Btn = customtkinter.CTkButton(master=frame , text='<', corner_radius=30 , font=('Roboto', 24), command=pre_image, height=32)
previous_Img_Btn.place(x= 480, y= 600)

denied_Btn = customtkinter.CTkButton(master=frame , text='Denied', corner_radius=18 , font=('Roboto', 24), fg_color=('red','red'), command=denied, width=170, height=32)
denied_Btn.place(x=700, y=600)

approval_Btn = customtkinter.CTkButton(master=frame , text='Approved', corner_radius=18 , font=('Roboto', 24), fg_color=('green','green'), command=approved, width=170, height=32)
approval_Btn.place(x=940, y=600)

next_Img_Btn = customtkinter.CTkButton(master=frame , text='>', corner_radius=30 , font=('Roboto', 24), command=next_image, height=32)
next_Img_Btn.place(x=1190, y=600)

# Binding keys to the root window
root.bind('<f>' , pre_image)
root.bind('<g>', denied)
root.bind('<h>' , approved)
root.bind('<j>' , next_image)

# Initializing the first image loading 
update_image()

root.mainloop()
