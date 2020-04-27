from django.db import models

class Invite(models.Model):
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=300)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    RACE_CHOICES = (
        ("ASIAN", "Asian"),
        ("BLACK", "Black"),
        ("LATINO", "Latino"),
        ("WHITE", "White"),
        ("OTHER", "Other"),
        ("?", "Unknown"),
    )
    race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default="?"
    )
    notes = models.TextField(blank=True)
