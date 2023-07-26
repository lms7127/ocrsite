from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
import os
import cv2
import easyocr
import logging

@csrf_exempt
def index(request):
    
    return render(request, 'inpimg/home.html')

tar=0
con='en'
last_image=''

@csrf_exempt   
def upload(request):
    return render(request,'inpimg/upload.html')

@csrf_exempt  
def upload_create(request):
    global tar
    tar+=1
    form=Profile()
    form.country=request.POST['country']
    try:
        form.image=request.FILES['image']
        form.id=tar
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    
    
    return redirect('/inpimg/profile/')  


@csrf_exempt  
def profile(request):
    global tar, con, last_image
    
    
    
    profile=Profile.objects.get(id=tar) 
    if last_image!='':
        os.remove(last_image.path)
    last_image=profile.image
    
    image = profile.image.url
    con=profile.country
    
    currentPath = os.getcwd()
    results=[]
    reader = easyocr.Reader([con], gpu=True)
    
    THRESHOLD = 0.01
    
    
    result = reader.readtext(currentPath+image)
    
    for bbox, text, conf in result:
        if conf > THRESHOLD:
            results.append(text)
    
        
    return render(request,'inpimg/home.html',{'profile':profile, 'results':results})


