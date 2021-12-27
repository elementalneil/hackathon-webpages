from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    roll = models.CharField(max_length=9)
    branch = models.CharField(max_length=4)
    mobile = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.name