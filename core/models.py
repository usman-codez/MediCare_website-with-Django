from django.db import models

# Create your models here.
class Doctor(models.Model):
    d_name = models.CharField(max_length=70)
    d_id = models.IntegerField()
    d_email = models.EmailField()
    d_hos = models.CharField(max_length=70)
    comment = models.CharField(max_length=200,default='hello')

    def __str__(self):
        return self.d_name


