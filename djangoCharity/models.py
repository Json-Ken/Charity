from django.db import models


# Create your models here.
class donar(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=1000, blank=False, null=False)
    location = models.CharField(max_length=1000,)

    def __str__(self):
        return self.name