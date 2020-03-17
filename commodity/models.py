# -*- coding: utf-8 -*-
from django.db import models

class Commodity(models.Model):
    name = models.CharField(max_length = 30)
    intro = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    disc_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    publish_time = models.DateTimeField(auto_now = False, auto_now_add = True)
    TYPE_CHOICE = {('FD', '食品'), ('CL', '衣物'), ('EL', '电器'), ('DG', '数码'), ('DU', '日用'),('JE', '首饰'),('MD', '药品'),}
    commodity_type = models.CharField(max_length = 4, choices = TYPE_CHOICE)
    commodity_id = models.CharField(max_length = 20, unique = True)
    edition = models.CharField(max_length = 100, null = True)
    
    def __str__(self):
        return self.name
