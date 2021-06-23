from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    S_id = models.CharField(max_length=10)


    def __str__(self):
        return self.firstname
