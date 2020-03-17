from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 30,)
    account = models.CharField(max_length = 10, unique = True)
    password = models.CharField(max_length = 40)
    address = models.CharField(max_length = 50)
    telephone = models.DecimalField(max_digits = 11, decimal_places = 0)
    credit = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
