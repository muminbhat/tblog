from django.db import models

# Create your models here.
class Contact(models.Model):
    message = models.TextField()
    email = models.EmailField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.EmailField()
        
    def __str__(self):
        return self.email