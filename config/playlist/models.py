from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length = 200)
    embed_code = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title