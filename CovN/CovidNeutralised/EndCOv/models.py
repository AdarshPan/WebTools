from django.db import models

# Create your models here.
class Members(models.Model):
    Image = models.ImageField(upload_to='media')
    # Id=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.Image)
