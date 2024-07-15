from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video, Comment
from .forms import VideoForm, CommentForm

def home_page(request):
    videos = Video.objects.all()
    return render(request, 'index.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    comments = video.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.video = video
            comment.comment_user = request.user
            comment.save()
            return redirect('video_detail', pk=video.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'video_detail.html', {'video': video, 'comments': comments, 'comment_form': comment_form})

@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form})

