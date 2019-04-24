from django.db import models

# Create your models here.

class Member(models.Model):
    Sl = models.CharField(max_length=40)
    Name = models.CharField(max_length=40)
    Diseases = models.CharField(max_length=40)
    Price = models.CharField(max_length=40)
    Available = models.CharField(max_length=40)

    #def __str__(self):
        #return self.firstname + " " + self.lastname