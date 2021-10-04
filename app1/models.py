from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dateofjoining = models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save()
