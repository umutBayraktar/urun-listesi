from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    pride = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()
