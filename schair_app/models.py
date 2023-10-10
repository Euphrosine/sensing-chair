from django.db import models

class SchairData(models.Model):
    datetime = models.DateTimeField()
    activity = models.CharField(max_length=100)

    def __str__(self):
        return self.activity

class Advice(models.Model):
    activity = models.OneToOneField('SchairData', on_delete=models.CASCADE)
    advice_text = models.TextField()

    def __str__(self):
        return self.activity.activity


