# Generated by Django 2.2.1 on 2019-06-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='trade_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
