from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    author = models.CharField(max_length=50)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=40)
    content = models.CharField(max_length=40)
    post = models.ForeignKey('Post', related_name='comment', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.author
