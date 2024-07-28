from django.shortcuts import render,HttpResponse,Http404
from django.contrib import messages
from pytube import YouTube
from django.http import FileResponse
from pathlib import Path
import re
#from tqdm import tqdm
#import time
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
#Create your views here.
def home(request):
    return render(request,"index.html")
def index(request):
    return render(request,"index.html")
def service(request):
    try:
        if request.method=="POST":
            url=request.POST.get("name", None)
            #messages.info(request,message="Download processing.. please wait..")
            print(url)
            #download(url)
            
                #SAVE_PATH= str(Path.home() / "Downloads")

                #yt=YouTube(url)
                #video=yt.streams.first()
                #video.download(SAVE_PATH)
            #yt = YouTube(url).streams.first()
            YouTube(url).streams.first().download()
            print("yt")
            #video_stream = yt.streams
            print("stream")

            #return FileResponse(open(YouTube(url).streams.first().download(skip_existing=True),'rb'),as_attachment=True)
            
            #message="Successfully Downloaded...."
    
    except Exception as e:
        print("error: ",e)
        return HttpResponse("Something went wrong..... check your url or check your connection.")
#def download(url):
    
    #SAVE_PATH= str(Path.home() / "Downloads")

    #yt = YouTube(url) 
    
    #video=yt.streams.first() #it will fetch the first stream of the video
    #video.download(SAVE_PATH)
    #video.download()