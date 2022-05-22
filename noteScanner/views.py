
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .apiToReadText import *
def noteScanner(request):
    if request.method == 'POST':
        form = fake(request.POST, request.FILES)
        form2 = fake2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("processImage")
        if form2.is_valid():
            form2.save()
            return redirect("processImage")
    else:
        form = fake()
        form2 = fake2()
    return render(request, 'takePicture.html', {'form' : form,'form2' : form2})

  
  
def success(request):
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        pictures = Image.objects.all() 
        index = len(pictures)-1
        image = pictures[index]
        print(image.action)
        if(image.action == "uploadFile"):
            a = pictureOfText(image.main_Img.url)
            a.uploadFile()
            context = {"title":a.title,"folder":a.folder,"source":a.destination}
            return render(request, 'showFile.html', context)
        elif(image.action == "uploadText"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.uploadText(True)
            print(a.textUploaded)
            a.textUploaded = a.textUploaded.split("\n")
            print(a.textUploaded)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.textUploaded,"source":image.main_Img.url}
            return render(request, 'showText.html', context)
        elif(image.action == "translate"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.translateText(False)
            print(a.translatedText)
            a.translatedText = a.translatedText.split("\n")
            if(a.origLang == a.docLang):
                return render(request, 'noLangFoundError.html', context)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.translatedText,"origLang":a.origLang,"docLang":a.docLang,"source":image.main_Img.url}
            return render(request, 'showTranslatedText.html', context)
        elif(image.action == "uploadTranslate"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.translateText(True)
            print(a.translatedText)
            a.translatedText = a.translatedText.split("\n")
            print(a.translatedText)
            if(a.origLang == a.docLang):
                return render(request, 'noLangFoundError.html', context)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.translatedText,"origLang":a.origLang,"docLang":a.docLang,"source":image.main_Img.url}
            return render(request, 'showTranslatedText.html', context)
        elif(image.action == "readText"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.readText(False)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.textUploaded.split("\n"),"destination":a.destination,"source":image.main_Img.url}
            return render(request, 'readTextOutLoud.html', context)
        elif(image.action == "readTextUpload"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.readText(True)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.textUploaded.split("\n"),"destination":a.destination,"source":image.main_Img.url}
            return render(request, 'readTextOutLoud.html', context)
        elif(image.action == "readTranslation"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.readTranslatedText(False)
            a.translatedText = a.translatedText.split("\n")
            if(a.origLang == a.docLang):
                return render(request, 'noLangFoundError.html', context)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.translatedText,"origLang":a.origLang,"docLang":a.docLang,"destination":a.destination,"source":image.main_Img.url}
            return render(request, 'readTranslationOutLoud.html', context)
        elif(image.action == "readTranslationUpload"):
            a = pictureOfText(image.main_Img.url)
            context = {"source":image.main_Img.url}
            if(not a.textExists):
                return render(request, 'noTextError.html', context)
            a.readTranslatedText(True)
            a.translatedText = a.translatedText.split("\n")
            if(a.origLang == a.docLang):
                return render(request, 'noLangFoundError.html', context)
            context = {"title":a.title,"folder":a.folder,"uploadText":a.translatedText,"origLang":a.origLang,"docLang":a.docLang,"destination":a.destination,"source":image.main_Img.url}
            return render(request, 'readTranslationOutLoudAndUpload.html', context)           
        else:
            return render(request, 'display_hotel_images.html', {'image' : pictures[index]})
def processImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form' : form})
