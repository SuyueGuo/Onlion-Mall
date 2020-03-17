# -*- coding: utf-8 -*-
from django.db import models

class History(models.Model):
    times = models.IntegerField()
    content = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.content


class User_History(models.Model):
    times = models.IntegerField()
    commodity = models.ForeignKey('commodity.Commodity', on_delete = models.CASCADE, )
    user = models.ForeignKey('user.User', on_delete = models.CASCADE, )

