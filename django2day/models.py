from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    mobilenumber=models.IntegerField(null=True)
    joined_date=models.DateField(null=True)

    def __str__ (self):
        return f"{self.firstname} {self.lastname}"

class Beginning(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
