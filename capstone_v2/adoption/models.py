from django.db import models

class Breed(models.Model):
    breed = models.CharField(max_length=100)
    endurance = models.BooleanField(default = False)
    id = models.PositiveIntegerField(primary_key = True, unique = True)

    def __str__(self):
        return self.breed
    
    class Meta:
        ordering = ['breed']

class Activity(models.Model):
    activity = models.CharField(max_length=100)
    breed = models.ManyToManyField(Breed, related_name='breeds')

    def __str__(self):
        return self.activity
