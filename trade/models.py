from django.db import models

class Trade(models.Model):
    commodity = models.ForeignKey('commodity.Commodity', on_delete = models.CASCADE, )
    user = models.ForeignKey('user.User', on_delete = models.CASCADE, )
    number = models.IntegerField()
    total_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    time = models.DateTimeField(auto_now = False, auto_now_add = True)
    trade_id = models.CharField(max_length = 20)
    STATE_CHOICE = {('0', '未付款'), ('1', '待发货'), ('2', '待确认'), ('3', '待评价'), ('4', '已完成'),('5', '退款/售后'), ('6', '已关闭')}
    state = models.CharField(max_length = 10, choices = STATE_CHOICE, default = 0)
    edition = models.CharField(max_length = 20, null = True)
    edition_id = models.CharField(max_length = 2, null = True)
