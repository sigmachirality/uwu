from django.db import models

#TODO: Add model validations.
class Club(models.Model):
    name = models.TextField()
    description = models.TextField()

    quality = models.DecimalField(decimal_places=1, max_digits=2)
    time_commitment = models.DecimalField(decimal_places=1, max_digits=2)
    fun = models.DecimalField(decimal_places=1, max_digits=2)

class Member(models.Model):
    name = models.TextField()
    clubs = models.ManyToManyField(Club, related_name="members")

class Comment(models.Model):
    content = models.TextField()
    commenter = models.ForeignKey(Member, on_delete=models.CASCADE \
        , related_name="comments")
    clubs = models.ForeignKey(Club, on_delete=models.CASCADE \
        , related_name="comments")