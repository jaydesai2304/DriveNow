from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=150)
    fullname = models.CharField(max_length=150, default="")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=8)
    confirmpassword = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.username}"
