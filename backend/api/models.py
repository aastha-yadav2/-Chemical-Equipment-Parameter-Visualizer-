from django.db import models

class Dataset(models.Model):
    file = models.FileField(upload_to='csvs/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dataset {self.id}"
