from django.db import models

# Create your models here.

class Course(models.Model):
    units= models.CharField(max_length=12, null=True, blank=True)
    student_name =models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student_name} {self.units}"