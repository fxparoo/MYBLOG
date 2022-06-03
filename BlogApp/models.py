from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    comment = models.ForeignKey('POST', max_length=40, on_delete=models.CASCADE)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=40)
    body = models.CharField(max_length=40)

    def __str__(self):
        return self.author

