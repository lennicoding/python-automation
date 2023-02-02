import os
from PIL import Image
import shutil

source_dir = "/Users/Admin/Downloads"
image_source_dir = "/Users/Admin/Downloads/Images"

with os.scandir(source_dir) as entries:
    for entry in entries:
        file_name, file_extension = os.path.splitext(entry.name)
        if file_extension == ".jpg":
            im1 = Image.open(source_dir + "/" + entry.name)
            im1.save(source_dir + "/" + entry.name[:-3] + ".png")
            os.remove(source_dir + "/" + entry.name)
        elif file_extension == ".jpeg":
            im1 = Image.open(source_dir + "/" + entry.name)
            im1.save(source_dir + "/" + entry.name[:-4] + ".png")
            os.remove(source_dir + "/" + entry.name)
        elif file_extension == ".svg":
            im1 = Image.open(source_dir + "/" + entry.name)
            im1.save(source_dir + "/" + entry.name[:-3] + ".png")
            os.remove(source_dir + "/" + entry.name)
