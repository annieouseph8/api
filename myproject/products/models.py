from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    availability = models.IntegerField(default=0)  # Assuming availability is stored as an integer

    def __str__(self):
        return self.name
