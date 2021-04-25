from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=40)
    loc=models.CharField(max_length=40)

    def __str__(self):
        return self.name