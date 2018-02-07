from django.db import models

# Create your models here.
class record(models.Model):
    flow = models.CharField(max_length=5)
    item = models.CharField(max_length=20)
    amount = models.IntegerField()
    paytype = models.CharField(max_length=10, blank=True, default='')
    tags = models.CharField(max_length=40, blank=True, default='')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.item