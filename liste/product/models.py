from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    prive = models.DecimalField()
    description = models.TextField()
