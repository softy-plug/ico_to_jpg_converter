import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
ico_folder = askdirectory(title='Select folder with ico images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the ico folder
for file_name in os.listdir(ico_folder):
    if file_name.endswith('.ico') or file_name.endswith('.ICO'):
        # open ico image and convert to png
        ico_image = Image.open(os.path.join(ico_folder, file_name))
        png_image = ico_image.convert('RGBA')

        # create new jpg file name
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)

        # save jpg image with maximum quality
        png_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All ico images in {ico_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug