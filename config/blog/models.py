from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 70)
    text = models.TextField()
    image = models.ImageField(upload_to = 'images/', default = 'none')
    likes = models.IntegerField(blank = True, default = 0)
    rating = models.FloatField(blank = True, default = 0)
    is_published = models.BooleanField(default = True)
    create_at = models.DateTimeField(auto_now_add = True)