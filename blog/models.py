from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Post(models.Model):
    User = get_user_model()
    author = models.ForeignKey(User, default='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Blog(models.Model):
    name = models.CharField(max_length=200, null=False,blank=False)
    description = models.TextField(default="Info about this blog",blank=True,null=True)
    published_date = models.DateField(default=timezone.now,blank=True, null=True)
    User = get_user_model()
    author = models.ForeignKey(User,default='User', on_delete=models.CASCADE)
    posts = models.ForeignKey(Post,null=True,blank= True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
