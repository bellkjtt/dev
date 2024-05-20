from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    body= models.TextField()
    
    tag = models.ManyToManyField('Tag', null=True, blank=True)
    
    def __str__(self):
    	return self.title
 
class Tag(models.Model):
     name = models.CharField(max_length=50, unique=True)
     
     def __str__(self):
         return self.name
 
 
class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    author= models.CharField(max_length=20)
    message= models.TextField()
    created= models.DateField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    def __str__(self):
	    return self.author
 
 
class User(models.Model):
     name = models.CharField(max_length=50)
     
     def __str__(self):
         return self.name
     
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)