from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class Booking(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.service}"