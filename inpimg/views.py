# -*- coding: utf-8 -*- 
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
import numpy as np
import os
import cv2
import easyocr
import logging
import urllib
#-*- coding: utf-8 -*-


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

    image = profile.image.url
    
    con=profile.country
    
    currentPath = os.getcwd()
    results=[]
    reader = easyocr.Reader([con], gpu=True)
    
    THRESHOLD = 0.1
    
    try:
        last=Profile.objects.get(id=tar-1)
        last_image=last.image.url
        os.remove(currentPath+last_image)
    except:
        pass
    
    
    
    
    try:
        result = reader.readtext(currentPath+image)
        for bbox, text, conf in result:
            if conf > THRESHOLD:
                results.append(text)
    except:    # 예외가 발생했을 때 실행됨
        results=['이미지를 다시 입력해주세요.']
        profile=None
    
        
    return render(request,'inpimg/result.html',{'profile':profile, 'results':results})

