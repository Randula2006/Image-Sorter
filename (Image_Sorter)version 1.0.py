import customtkinter
import tkinter
import os
from PIL import Image
import shutil
from pathlib import Path

# changing the directory to the folder with the images
os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image Sorter - Github\Image-Sorter\images')
# have to change the file path when changing the directory 


image_num =  int(input("enter the first value of the image you have")) #this will be replaced with the image renamer files and automatically add the image first value
    
def denied(event = None):
    global image_num
    # creating a folder named to_be_deleted or if exists send the image to that folder
    # no need to add as chdir mentioned images 
    deletion_folder = 'To_Be_Deleted'
    os.makedirs(deletion_folder, exist_ok=True)
    shutil.move('{}_IMG.JPG'.format(image_num) , deletion_folder)
    
    image_num += 1  
    print('image has sent to To_Be_Deleted folder')
    update_image()
        
    return image_num
    

def approved(event = None):
    global image_num
    
    approval_folder = 'Approved_files'
    os.makedirs(approval_folder, exist_ok=True)
    shutil.move('{}_IMG.JPG'.format(image_num) , approval_folder)
    
    image_num += 1
    print('image has been Approved_files folder')
    update_image()   
    
    return image_num


def pre_image(event = None):
    global image_num
    
    image_num = image_num - 1
    print('pevious image')
    update_image()   
    
    return image_num


def next_image(event = None):
    global image_num
    
    image_num += 1
    print('next image')
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

image_value = customtkinter.CTkEntry(master= frame , placeholder_text="Enter the first value of the image you have (ex:- 569)", width=250 , height=45)
image_value.place(x=200 , y= 330)


#binding keys to the root window

root.bind('<f>' , pre_image)
root.bind('<g>' , denied)
root.bind('<h>' , approved)
root.bind('<j>' , next_image)

# initializing the first image loading 
update_image()

root.mainloop()