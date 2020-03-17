from django.db import models

class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete = models.CASCADE)
    commodity = models.ForeignKey('commodity.Commodity', on_delete = models.CASCADE)
    score = models.IntegerField()
    content = models.CharField(max_length = 1000)
    create_time = models.DateTimeField(auto_now = False, auto_now_add = True)
    trade_id = models.CharField(max_length = 20, null = True)
