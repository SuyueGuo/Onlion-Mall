# Generated by Django 2.2.1 on 2019-05-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20190523_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='state',
            field=models.CharField(choices=[('0', '未付款'), ('5', '退款/售后'), ('1', '待发货'), ('4', '已完成'), ('3', '待评价'), ('2', '待确认'), ('6', '已关闭')], default=0, max_length=10),
        ),
    ]