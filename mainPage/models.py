from django.db import models



class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class MainPageSlider(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.title
    

class ExperienceSection(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='experience')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')  
    description = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name
    

class About(models.Model):
    description = models.TextField(blank=True, null=True) 
