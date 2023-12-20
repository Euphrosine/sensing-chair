from django.db import models

class SchairData(models.Model):
    datetime = models.DateTimeField()
    activity = models.CharField(max_length=100)

    def __str__(self):
        return self.activity

class Advice(models.Model):
    schair_data = models.OneToOneField(SchairData, on_delete=models.CASCADE, primary_key=True)
    advice_text = models.TextField()

    def __str__(self):
        return self.schair_data.activity

#ml model

class PostureData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    posture_status = models.IntegerField()

    def __str__(self):
        return f"PostureData - {self.timestamp}"
