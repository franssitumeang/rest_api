from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title
