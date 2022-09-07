from django.db import models

# Create your models here.

class player(models.Model):
    slotId = models.IntegerField()
    playerChoose = models.IntegerField()
    uniqueKey = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    dateAdded = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    
class evening(models.Model):
    slotId = models.IntegerField()
    playerChoose = models.IntegerField()
    uniqueKey = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    dateAdded = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    
