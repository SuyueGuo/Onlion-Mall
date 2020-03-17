from django.db import models

class Shopping_Cart(models.Model):
        commodity = models.ForeignKey('commodity.Commodity', on_delete = models.CASCADE, )
        user = models.ForeignKey('user.User', on_delete = models.CASCADE, )
        number = models.IntegerField()
        edition = models.CharField(max_length = 20, null = True)
        edition_id = models.CharField(max_length = 2, null = True)
