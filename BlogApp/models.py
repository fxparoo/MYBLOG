from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=40)
    content = models.TextField(blank=Tru, null=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
