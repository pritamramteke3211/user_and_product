from django.db import models
from django.utils.timezone import now

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True)
    category = models.CharField(max_length=30,blank=True)
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=1000,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    parent = models.IntegerField(blank=True,default=0) ## parent is field of self.model 
  
    reply = models.BooleanField(default=False,null=True)
    reply_count = models.IntegerField(blank=True,default=0)

    timestamp = models.DateTimeField(default=now) ## don't need add time when comment submitted

    def __str__(self):
        return str(self.sno)