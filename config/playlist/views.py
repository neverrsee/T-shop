from django.shortcuts import render, redirect
from .models import Video

# Create your views here.

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'playlist/video_list.html', {'videos':videos})

def video_create(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        embed_code = request.POST.get('embed_code')
        Video.objects.create(title = title,
            embed_code = embed_code,)
        return redirect('video_list')
    return render(request, 'playlist/create_video.html', )