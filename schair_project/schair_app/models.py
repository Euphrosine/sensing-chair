from django.db import models

class SchairData(models.Model):
    datetime = models.DateTimeField()
    activity = models.CharField(max_length=100)

class Advice(models.Model):
    activity = models.CharField(max_length=100, unique=True)
    advice = models.TextField()

    def __str__(self):
        return self.activity
