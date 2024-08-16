from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp
import os

def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            try:
                
                home_dir = os.path.expanduser("~")
                download_dir = os.path.join(home_dir, "Downloads")
                ydl_opts = {
                    'outtmpl': f'{download_dir}/%(title)s.%(ext)s',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                return render(request, 'download_success.html',{'download_dir': download_dir})
            except Exception as e:
                return HttpResponse(f"Error: {e}")
        else:
            return HttpResponse("Please enter a valid URL.")
    return render(request, 'index.html')
