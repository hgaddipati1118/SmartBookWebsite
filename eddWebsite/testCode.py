# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:10:43 2022

@author: hgadd
"""


from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
   
# For using listdir()
import os
   
  
# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
   
# replace the value of this variable
# with the absolute path of the directory

folderName = 'testFolder'  # Please set the folder name.
folderID = 0

folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
for folder in folders:
    if folder['title'] == folderName:
        folderID = folder['id']
    
while(folderID == 0):
    folder = drive.CreateFile({'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            folderID = folder['id']
print(folderID)

path = r"C:\Users\hgadd\eddWebsite\media\static\noteScanner\input"   
   
# iterating thought all the files/folder
# of the desired directory
for x in os.listdir(path):
   
    f = drive.CreateFile({'parents': [{'id': folderID}]})
    f.SetContentFile(os.path.join(path, x))
    f.Upload()
  
    # Due to a known bug in pydrive if we 
    # don't empty the variable used to
    # upload the files to Google Drive the
    # file stays open in memory and causes a
    # memory leak, therefore preventing its 
    # deletion
    f = None