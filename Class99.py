import os
import shutil

source=input("Enter Your Source Folder Name:")
Destination=input("Enter Destination Folder Name:")

source= source +'/'
Destination= Destination +'/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),Destination) 