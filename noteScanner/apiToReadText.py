# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:14:43 2022

@author: hgadd
"""
from gtts import gTTS 
import os
import json
import shutil
import requests
import pathlib
import re
import difflib
from .languageCodes import *
from datetime import datetime
from .googleCloudCode import getTextFromPicture
from deep_translator import GoogleTranslator
from langdetect import detect
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
# Below code does the authentication
from PIL import Image as funkyDunk
# part of the code
print(os.getcwd())
gauth = GoogleAuth()
  # Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)

source_dir = r"media\static\noteScanner\input"
outputDirectory = r"media\static\noteScanner\output"
print(os.getcwd())
os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
print(os.getcwd())
class pictureOfText:
    def __init__(self, fileName):
        fileNameArray = fileName.split("/")
        fileNameArrayIndex = len(fileNameArray)-1
        self.fileName = fileNameArray[fileNameArrayIndex]
        filePath = source_dir + str('\\') + str(self.fileName)
        if ("SmartBook" in fileName):
            original_img = funkyDunk.open(filePath)
            # Flip the original image horizontally
            horz_img = original_img.transpose(method=funkyDunk.FLIP_LEFT_RIGHT)
            horz_img = horz_img.convert('RGB')
            horz_img.save(filePath)
            
            # close all our files object
            original_img.close()
            horz_img.close()
        self.fileExtension = pathlib.Path(filePath).suffix
        self.fileTitle = self.fileName.split(self.fileExtension)[0]
        a = getTextFromPicture(filePath)
        self.pictureText = a
        print(a)
        self.textExists = False
        if(len(a)>0):
            self.textExists = True
        
    def __str__(self):
        return self.pictureText
    def getTitleAndFolder(self): 
        titleArray=re.findall("#[^#]+#", self.pictureText)
        if(len(titleArray)>0):
            self.title = titleArray[0].replace("#","")
            self.title = self.title.strip()
        else:
            self.title = False
        folderArray=re.findall("%[^%]+%", self.pictureText)
        if(len(folderArray)>0):
            self.folder = folderArray[0].replace("%","")
            self.folder = self.folder.strip()
        else:
            self.folder = False
        """if(self.folder != False):
            print("here")
            if(" " in self.folder):
                print("Error! There is a space in your folder name")
                print("The folder your file with be put into is " + self.folder.replace(" ", ""))
                print("press 1 to continue with this, press 2 if you wish to change the folder name, press any other key if you wish to have no folder")
                val = int(input(""))
                if val == 1:
                    self.folder = self.folder.replace(" ", "")
                elif val == 2:
                        print ("Type in your new folder name")
                        self.folder = input("")
                else:
                    return
    
            destination = outputDirectory + "\\" + self.folder
            if not os.path.exists(destination):
                os.makedirs(destination)"""
    def getFolderID(self):
        folderID = 0
        folderName = self.folder
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
        self.folderID = folderID
    def uploadFile(self):
        source = source_dir + "\\" + self.fileName
        destination = outputDirectory
        self.getTitleAndFolder()
        if(self.title == False):
            self.title = self.fileTitle
        self.source = source
        if(self.folder != False):
            self.getFolderID()
            f = drive.CreateFile({'title':self.title,'parents': [{'id': self.folderID}]})
            f.SetContentFile(source)
            f.Upload()
        else:
            f = drive.CreateFile({'title':self.title})
            f.SetContentFile(source)
            f.Upload()

            
        """now = datetime.now()
            dt_string = now.strftime("%d%m%Y%H%M%S%MS")
            destination += "\\" + dt_string """
        destination += "\\" +self.title +  self.fileExtension
        shutil.copy(source, destination)
        self.destination = r"/media/static/noteScanner/output/" + self.title + self.fileExtension
        print("File uploaded")
    def uploadText(self,upload):
        self.getTitleAndFolder()
        destination = outputDirectory
        textToUpload = str(self.pictureText)
        if(self.folder != False):
            folderArray=re.findall("%[^%]+%", self.pictureText)
            textToUpload = textToUpload.replace(folderArray[0],"")
        if(self.title != False):
            titleArray=re.findall("#[^#]+#", self.pictureText)
            textToUpload = textToUpload.replace(titleArray[0],"")
        else:
            now = datetime.now()
            dt_string = now.strftime("%d%m%Y%H%M%S%MS")
        self.textUploaded = textToUpload.strip()
        if(self.title == False):
            self.title = self.fileTitle
        if upload:
            if(self.folder != False):
                self.getFolderID()
                f = drive.CreateFile({'title': self.title + ".txt", 'parents': [{'id': self.folderID}],'mimeType': 'text/plain'})
                f.SetContentString(self.textUploaded)
                f.Upload(param={'convert': True})
            else:
                f = drive.CreateFile({'title': self.title,'mimeType': 'text/plain'})
                f.SetContentString(self.textUploaded)
                f.Upload(param={'convert': True})
        print("file uploaded as text")
    def translateText(self,upload):
        self.origLang = languageShortNames[detect(self.pictureText)]
        self.origLangShortCode = detect(self.pictureText)
        self.getTitleAndFolder()
        destination = outputDirectory
        translationArray=re.findall("\?\?[^%]+\?\?", self.pictureText)
        if len(translationArray)>0:
            languageToTranslate = translationArray[0].replace("??","")
            self.languageShortCode = findLanguageShortCode(languageToTranslate)
        else:
            self.languageShortCode = self.origLangShortCode
        self.docLang = languageShortNames[self.languageShortCode]
        textToUpload = str(self.pictureText)
        if(self.folder != False):
            folderArray=re.findall("%[^%]+%", self.pictureText)
            textToUpload = textToUpload.replace(folderArray[0],"")
            destination += "\\" + self.folder
        self.textDestination = destination
        if(self.title != False):
            titleArray=re.findall("#[^#]+#", self.pictureText)
            textToUpload = textToUpload.replace(titleArray[0],"")
            destination += "\\" + self.title
        if(self.languageShortCode != self.origLangShortCode):
            translationArray=re.findall("\?\?[^%]+\?\?", self.pictureText)
            textToUpload = textToUpload.replace(translationArray[0],"")
        translatedText = GoogleTranslator(source='auto', target=self.languageShortCode).translate(textToUpload)
        self.translatedText = translatedText.strip()
        self.destination = destination
        destination += ".txt"
        if(self.title == False):
            self.title = self.fileTitle
        if upload:
            if(self.folder != False):
                self.getFolderID()
                f = drive.CreateFile({'title': self.title + ".txt", 'parents': [{'id': self.folderID}],'mimeType': 'text/plain'})
                f.SetContentString(self.translatedText)
                f.Upload(param={'convert': True})
            else:
                f = drive.CreateFile({'title': self.title,'mimeType': 'text/plain'})
                f.SetContentString(self.translatedText)
                f.Upload(param={'convert': True})
            print("file uploaded as text")
    def readText(self,upload):
        self.origLang = languageShortNames[detect(self.pictureText)]
        self.origLangShortCode = detect(self.pictureText)
        print("HI")
        self.uploadText(False)
        now = datetime.now()
        dt_string = "recording" + now.strftime("%d%m%Y%H%M%S%MS")
        print(self.origLangShortCode)
        speech = gTTS(text = self.textUploaded, lang = self.origLangShortCode, slow = False)
        self.mp3Destination = outputDirectory + "\\" + self.title + ".mp3"
        speech.save(self.mp3Destination)
        self.destination = r"/media/static/noteScanner/output/" + self.title + ".mp3"
        if upload:
            if(self.folder != False):
                self.getFolderID()
                f = drive.CreateFile({'title':self.title,'parents': [{'id': self.folderID}]})
                f.SetContentFile(self.mp3Destination)
                f.Upload()
            else:
                f = drive.CreateFile({'title':self.title})
                f.SetContentFile(self.mp3Destination)
                f.Upload()
    def readTranslatedText(self,upload):
        self.translateText(False)
        speech = gTTS(text = self.translatedText, lang = self.languageShortCode, slow = False)
        self.mp3Destination = outputDirectory + "\\" + self.title + ".mp3"
        speech.save(self.mp3Destination)
        self.destination = r"/media/static/noteScanner/output/" + self.title + ".mp3"
        if upload:
            if(self.folder != False):
                self.getFolderID()
                f = drive.CreateFile({'title':self.title,'parents': [{'id': self.folderID}]})
                f.SetContentFile(self.mp3Destination)
                f.Upload()
            else:
                f = drive.CreateFile({'title':self.title})
                f.SetContentFile(self.mp3Destination)
                f.Upload()

        
        
        