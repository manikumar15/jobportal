from django.db import models

# Create your models here.

class Search(models.Model):
    job= models.CharField(max_length=40,null=True)
    skills = models.CharField(max_length=40,null=True)
    experience =  models.CharField(max_length=40,null=True)
    contact = models.CharField(max_length=40,null=True)
    location = models.CharField(max_length=40,null=True)



    def __str__(self):
        return self.job

class Register(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    job = models.CharField(max_length=40,null=True)
    cv=models.FileField(upload_to='files/')
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class login(models.Model):
    
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    
    

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class applyjob(models.Model):
    
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=30)
    cv=models.FileField(upload_to='files/')
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name