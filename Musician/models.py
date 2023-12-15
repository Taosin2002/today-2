
from django.db import models

# Create your models here.
class Musician(models.Model):
    ID=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Phone_Number=models.CharField(max_length=50)
    Instrument_Type=models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name