from django.db import models
from django.conf import settings

class Video(models.Model):
    video_title = models.CharField(max_length=255)
    video_content = models.FileField(upload_to='videos/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

class Comment(models.Model):
    comment_text = models.TextField()
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'