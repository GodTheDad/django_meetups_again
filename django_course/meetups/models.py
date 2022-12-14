from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class Participant(models.Model):
    email = models.EmailField(unique= True)

    def __str__(self):
        return self.email


class Location(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length = 300)

    def __str__(self):
        return f'{self.name} ({self.address})'



class Meetup(models.Model):
    title = models.CharField(max_length=200, null = False)
    slug = models.SlugField(unique=True)
    description= models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    organizer_email = models.EmailField()
    participants = models.ManyToManyField(Participant, blank = True)
    date = models.DateField()


    def __str__(self):
        return self.title