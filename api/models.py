from django.db import models

# Create your models here.
class items(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    barcode = models.IntegerField(unique=True)

    def __int__(self):
        return self.id