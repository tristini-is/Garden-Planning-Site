from django.db import models
from django.urls import reverse


# Create your models here.
class Planter(models.Model):
    name = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('planter-detail', args=[str(self.id)])


class Plant(models.Model):
    name = models.CharField(max_length=200, blank = True)
    care = models.TextField(blank = True)
    plantDate = models.DateField()
    box = models.ForeignKey(Planter, on_delete=models.CASCADE, default = None, null=True, blank=True)
    def get_absolute_url(self):
        return reverse('plant-detail', args=[str(self.id)])
