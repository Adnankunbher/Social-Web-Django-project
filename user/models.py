from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    captions=models.TextField()
    image=models.ImageField(upload_to='post_images')
    published_date=models.DateField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) 

class LikePost(models.Model):
    user=models.ManyToManyField(User)
    post=models.OneToOneField(Post,on_delete=models.CASCADE)
    no_of_likes=models.IntegerField(default=0)

    @classmethod
    def like(cls,post,liking_user):
        obj, create=cls.objects.get_or_create(post=post)
        obj.user.add(liking_user)
    
    @classmethod
    def dislike(cls,post,disliking_user):
        obj,create=cls.objects.get_or_create(post=post)
        obj.user.remove(disliking_user)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profileimage=models.ImageField(upload_to="profile_images", default="adnan.jpg")
    location=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
