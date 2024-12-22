from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    quantity = models.IntegerField()
    ordering = models.FloatField(default=0) 

    def __str__(self):
        return self.title


class RSVP(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    presence = models.CharField(max_length=1000)
    food = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.surname}"