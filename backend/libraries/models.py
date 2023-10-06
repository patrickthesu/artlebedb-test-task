from django.db import models


class Coordinates(models.Model):
    posx = models.DecimalField(max_digits=12, decimal_places=8)
    posy = models.DecimalField(max_digits=12, decimal_places=8)

class Contacts(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)

class Library(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    name = models.CharField(max_length=250)
    description = models.TextField()
    fullAdress = models.CharField(max_length=500)
    coordinates = models.ForeignKey(
        "Coordinates",
        on_delete=models.CASCADE,
    )
    contacts = models.ForeignKey(
        "Contacts",
        on_delete=models.CASCADE,
    )
