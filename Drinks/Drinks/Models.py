from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)