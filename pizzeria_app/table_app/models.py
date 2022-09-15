from django.db import models
from django.utils import timezone
from random import randint


class booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    booking_date = models.DateField(max_length=255, blank=True, null=True)
    booking_ToD = models.TimeField(max_length=255, blank=True, null=True)
    number_of_guests = models.IntegerField()
    phone_number = models.CharField(max_length=1024)
    special_request = models.TextField(blank=True, max_length=1024)
    booking_reference = models.CharField(max_length=50)

    class Meta:
        ordering = ["-last_name"]

    def __str__(self):
        return self.first_name


class contact(models.Model):
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=256, blank=True)
    message = models.TextField(blank=True)

    class Meta:
        ordering = ["-email"]

    def __str__(self):
        return self.name
