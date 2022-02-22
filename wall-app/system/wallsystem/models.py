from django.db import models

# Create your models here.

class Wall(models.Model):
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.message