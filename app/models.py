from django.db import models

# Create your models here.

class Vizag_places(models.Model):
    Placename = models.CharField(max_length=100)
    Placelocation = models.CharField(max_length=100)
    Placemg_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Placename
    
     
