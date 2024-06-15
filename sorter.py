import customtkinter
import tkinter
import os
from PIL import Image
import shutil
from pathlib import Path

# changing the directory to the folder with the images
os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image Sorter - Github\Image-Sorter\images')
# have to change the file path when changing the directory 



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
        # trying to fix if the files are already have the correct format 
         file_name_without_ext, file_ext = os.path.splitext(file_name)
         parts = file_name_without_ext.strip().split('_')
        #  the below two lines of code can sometimes break the function as they will  not output the correct format 
         file_num , clear_file = parts
         file_names_reordered = f'{file_num}_{clear_file}{file_ext}'
         os.rename(file_name, file_names_reordered)
         
         file_number_array
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
    image_num = lowest_number
    print(f"The lowest file number is: {lowest_number}")
else:
    print("No file numbers collected.")


##################################################################
# posible errors

# if the file is not chcked the value is not sent to the array of integers


# upper part =  file renamer 




# downside =  functioning the btns in GUI

def image_assecding():
    global image_num
    
    for num in file_number_array:
        if num > image_num:
            image_num = num
            break
        else:
            image_num = image_num
            print('problem exists-have to fix it')
            
    update_image()

def image_decending():
    global image_num
    
    for num in reversed(file_number_array):
        if num < image_num:
            image_num = num
            break
        else:
            image_num = image_num
            print('file is not decending')    
            
    update_image()
    

def denied(event = None):
    global image_num
    # creating a folder named to_be_deleted or if exists send the image to that folder
    # no need to add as chdir mentioned images 
    deletion_folder = 'To_Be_Deleted'
    os.makedirs(deletion_folder, exist_ok=True)
    shutil.move('{}_IMG.JPG'.format(image_num) , deletion_folder)
    
    # image_num += 1 
    
    if image_num not in file_number_array:
        image_assecding()
        
    print('image has sent to To_Be_Deleted folder')
    update_image()
        
    return image_num
    

def approved(event = None):
    global image_num
    
    approval_folder = 'Approved_files'
    os.makedirs(approval_folder, exist_ok=True)
    shutil.move('{}_IMG.JPG'.format(image_num) , approval_folder)
    
    # image_num += 1
    if image_num not in file_number_array:
        image_assecding()
        
    print('image has been sent to Approved_files folder')
    update_image()   
    
    return image_num


def pre_image(event = None):
    global image_num
    
    # image_num = image_num - 1
    
    print('pevious image')
    
    image_decending()
    update_image()   
    
    return image_num


def next_image(event = None):
    global image_num
    
    # image_num += 1
    
    print('next image')
    
    # image assending function 
    image_assecding() 
    update_image()
     
    return image_num
    
   
def update_image():
    global image_num , image_label
    
    image_path = '{}_IMG.JPG'.format(image_num)
    if os.path.exists(image_path):
        image = customtkinter.CTkImage(light_image=Image.open(image_path), size = (image_width , image_height))
        image_label.configure(image = image)
    else:
        print(f'Image {image_path} does not exists.')
        image_assecding()
        
        
        #add the file_number_array to go to the closest next file
        
        
        
 
# GUi area 

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme('dark-blue')


root = customtkinter.CTk()
# genaral dimensions 
root.geometry("1440x1280")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both" , expand=True)

label = customtkinter.CTkLabel(master=frame , text="Image Sorter - version 1.0", font= ("Roboto" , 40))
label.pack(pady=12 , padx=24)

# adding the images for slideshow

#image size height and width
image_width = int(750)
image_height = int(450)


# initialize the image (empty)
# don't have to add images to the file path as it is mentioned in the chdir section at the top
image_path = '{}_IMG.JPG'.format(image_num)
if os.path.exists(image_path):
    image  = customtkinter.CTkImage(light_image= Image.open(image_path), size = (image_width , image_height))
else:
    image = None
# label creation for the images


# (experimental code)-worked
image_label = customtkinter.CTkLabel(root, image=image, text='')
image_label.place(x=590, y=120)

# image = customtkinter.CTkImage(light_image = Image.open(image_path), size = (image_size , image_size))
# image_label = customtkinter.CTkLabel(root, image= image , text='')
# image_label.place(x=590, y=120)

previous_Img_Btn = customtkinter.CTkButton(master=frame , text='<', corner_radius=30 , font=('Roboto', 24), command=pre_image , height=32)
previous_Img_Btn.place(x= 480, y= 600)

denied_Btn = customtkinter.CTkButton(master=frame , text='Denied', corner_radius=18 , font=('Roboto', 24), fg_color=('red','red') , command= denied , width= 170 , height=32)
denied_Btn.place(x= 700, y= 600)

approval_Btn = customtkinter.CTkButton(master=frame , text='Approved', corner_radius=18 , font=('Roboto', 24) , fg_color=('green','green'), command=approved ,width= 170 , height=32)
approval_Btn.place(x= 940, y= 600)

next_Img_Btn = customtkinter.CTkButton(master=frame , text='>', corner_radius=30 , font=('Roboto', 24), command= next_image , height=32)
next_Img_Btn.place(x= 1190, y= 600)



#binding keys to the root window

root.bind('<f>' , pre_image)
root.bind('<g>' , denied)
root.bind('<h>' , approved)
root.bind('<j>' , next_image)

# initializing the first image loading 
update_image()

root.mainloop()