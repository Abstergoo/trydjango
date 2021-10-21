from django.db import models

class Products(models.Model): 
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True) 
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False)
# Create your models here.
