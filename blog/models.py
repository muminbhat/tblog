from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=250,
                            unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    read_time = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    hero_image = models.ImageField(blank=True)
    content = models.TextField()
    tags = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title + ' ' + '|'+ ' ' + self.author

