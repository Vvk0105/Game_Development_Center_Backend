from django.db import models

# Create your models here.
class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name