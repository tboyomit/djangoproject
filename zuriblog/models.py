from django.conf import settings # new2
from django.contrib.auth import get_user_model # new2

from django.db import models
from django.urls import reverse # new



class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model): # new2
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):          # new2
        return self.comment


    def get_absolute_url(self):     # new2
        return reverse('post_list')
