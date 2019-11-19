from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Note(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='list_tags')

    def __str__(self):
        return f'Title: {self.title}'
