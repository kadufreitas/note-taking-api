from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    #Add relação ao Client
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='list_tags', blank=True)

    def __str__(self):
        return f'Title: {self.title}'
