from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Languages(models.Model):
    name=models.CharField(max_length=30)
    paradigm=models.ForeignKey(Paradigm,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Programmer(models.Model):
    name=models.CharField(max_length=30)
    language=models.ManyToManyField(Languages)
