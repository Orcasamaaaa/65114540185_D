from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)