from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PlantFamily(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Plant(models.Model):
    name = models.CharField(max_length=150)
    height = models.IntegerField(models.DecimalField(max_digits=5, decimal_places=2))
    photos = models.ImageField(upload_to='photos/')
    family = models.ForeignKey(PlantFamily, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name