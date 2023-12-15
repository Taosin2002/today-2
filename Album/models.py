from django.db import models
from Musician.models import Musician

class Album(models.Model):
    Album_Name = models.CharField(max_length=50)
    Author = models.ForeignKey(Musician, on_delete=models.CASCADE)
    Album_Release_Date = models.DateField()
    Rating = models.FloatField(default=1)

    def __str__(self):
        return self.Album_Name
