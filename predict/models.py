from django.db import models

# Create your models here.


class Disease(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    symptoms= models.CharField(max_length=500)
    preventions=models.CharField(max_length=500)
    primarymedication=models.CharField(max_length=500)

    def __str__(self):
        return self.name
