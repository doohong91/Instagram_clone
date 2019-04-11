from django.db import models


class Post(models.Model):
    content = models.CharField(max_length = 140)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return '<{}: {}>'.format(self.id, self.content[:20])