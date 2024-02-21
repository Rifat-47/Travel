from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
    demo = models.CharField(max_length= 20)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField()
    def __str__(self):
        return self.name