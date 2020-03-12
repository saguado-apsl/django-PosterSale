from django.db import models


class Poster(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    cover = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name, self.description, self.price, self.cover)
