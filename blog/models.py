from django.db import models
from django.utils import timezone
from distutils.command.upload import upload

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    read_time = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    hero_image = models.ImageField(blank=True, upload_to='blog/assets')
    content = models.TextField()


