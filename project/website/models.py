from django.db import models

# Create your models here.

# models.py  
from django.db import models  

class Sidebar(models.Model):  
    title = models.CharField(max_length=200)  
    subtitle = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='sidebar_images/')  # تأكد من إعداد الوسائط (media)  

    def __str__(self):  
        return self.title


class MainAbout(models.Model):  
    title = models.CharField(max_length=200)  
    descriptions = models.TextField(max_length=200)  
    image = models.ImageField(upload_to='mainAbout_images/')  # تأكد من إعداد الوسائط (media)  

    def __str__(self):  
        return self.title





class Services(models.Model):  
    title = models.CharField(max_length=200)  
    descriptions = models.TextField(max_length=200)  
    image = models.ImageField(upload_to='mainAbout_images/')  # تأكد من إعداد الوسائط (media)  

    def __str__(self):  
        return self.title



class FAQ(models.Model):  
    question = models.CharField(max_length=255)  
    answer = models.TextField()  

    def __str__(self):  
        return self.question 
