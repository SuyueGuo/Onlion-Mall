# Generated by Django 2.2.1 on 2019-06-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20190531_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='state',
            field=models.CharField(choices=[('1', '待发货'), ('3', '待评价'), ('0', '未付款'), ('5', '退款/售后'), ('2', '待确认'), ('4', '已完成'), ('6', '已关闭')], default=0, max_length=10),
        ),
    ]
