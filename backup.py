
import customtkinter
import tkinter
import os
from PIL import Image


    
def denied(event = None):
    print( event)

def approved(event = None):
    print('image has been approved')

def pre_image(event = None):
    print('pevious image')

def next_image(event = None):
    print('next image')
    
   

    
# GUi area 

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme('dark-blue')


root = customtkinter.CTk()
root.geometry("500x350")


def login():
    print('test')
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both" , expand=True)

label = customtkinter.CTkLabel(master=frame , text="Image Sorter", font= ("Roboto" , 40))
label.pack(pady=12 , padx=24)

# adding the images for slideshow

# add images for the root window 
image_path = os.path.join(os.path.dirname(__file__), 'images/0818_IMG.JPG')

# label creation for the images
image_size = int(350)#image size height and width

image = customtkinter.CTkImage(light_image = Image.open(image_path), size = (image_size , image_size))
image_label = customtkinter.CTkLabel(root, image= image , text='')
image_label.place(x=590, y=120)

previous_Img_Btn = customtkinter.CTkButton(master=frame , text='<', corner_radius=30 , font=('Roboto', 24), command=pre_image)
previous_Img_Btn.place(x= 340, y= 600)

denied_Btn = customtkinter.CTkButton(master=frame , text='Denied', corner_radius=18 , font=('Roboto', 24), fg_color=('red','red') , command= denied)
denied_Btn.place(x= 540, y= 600)

approval_Btn = customtkinter.CTkButton(master=frame , text='Approved', corner_radius=18 , font=('Roboto', 24) , fg_color=('green','green'), command=approved)
approval_Btn.place(x= 740, y= 600)

next_Img_Btn = customtkinter.CTkButton(master=frame , text='>', corner_radius=30 , font=('Roboto', 24), command= next_image)
next_Img_Btn.place(x= 940, y= 600)


#binding keys to the root window

root.bind('<f>' , pre_image)
root.bind('<g>' , denied)
root.bind('<h>' , approved)
root.bind('<j>' , next_image)

root.mainloop()