from django.db import models


# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200, default="abc")

    def __str__(self):
        return self.name


class Location(models.Model):
    movie = models.ManyToManyField(Movies)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location