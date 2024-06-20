import os

os.chdir(r'C:\Users\Randula\Desktop\Programming\python\Rebooting\projects\Image sorter\images')

print(os.getcwd())

for file in os.listdir():
    file_name , file_ex = os.path.splitext(file)
   

    file_name.strip()
    clear_file , file_num = file_name.split('_')
    file_names_reordered =  '{}_{}{}'.format(file_num , clear_file , file_ex)

    os.rename(file , file_names_reordered)
    

        
    # item_num = 0
    # while item_num < int(listing_file_name[-1]):
        
    #     listing_file_name[0] = 'Image'
    #     listing_file_name[1] = item_num
    #     item_num += item_num
    #     print(listing_file_name)
    
    # reordered_list = [listing_file_name[1], listing_file_name[0]]
    
    

    
    
    
    