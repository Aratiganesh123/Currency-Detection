from email.mime import image
import os
import shutil

source_path = "/home/ignitarium/Currency-detection/normal/labels/10_Rupee"
dest_path =  "/home/ignitarium/Currency-detection/normal/labels/10_Rupee_Image"
image_path = "/home/ignitarium/Currency-detection/normal/images"

for filename in os.listdir(source_path):
    name = os.path.splitext(filename)[0]
    name += ".jpg"
    combined = os.path.join(image_path , name)
    combined_dest = os.path.join(dest_path , name)
    shutil.copy(combined , combined_dest)
   # print(combined)
