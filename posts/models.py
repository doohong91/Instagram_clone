from django.db import models
from django.conf import settings


class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    # User와의 YGGR 1 (1:N)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User와의 YGGR 2 (M:N)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    
    def __str__(self):
        return '<{}: {}>'.format(self.id, self.content[:20])


class Comment(models.Model):
    content = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    