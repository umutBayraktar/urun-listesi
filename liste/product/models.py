from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'pk': self.pk})

