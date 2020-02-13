from django.db import models

# Create your models here.
class employee(models.Model):
    Name  = models.CharField(max_length = 30)
    email = models.CharField(max_length =30)
    phoneNumber = models.IntegerField

    # def __str__(self):
    #     return self.Name

# to display all columns data in admin iterface, add a class in admin.py 

