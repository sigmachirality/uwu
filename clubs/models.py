from django.db import models


class Club(models.Model):
    name = models.TextField()
    description = models.TextField()

    quality = models.IntegerField()
    time_commitment = models.IntegerField()


class Member(models.Model):
    name = models.TextField(unique=True)
    clubs = models.ManyToManyField(Club, related_name="members")
