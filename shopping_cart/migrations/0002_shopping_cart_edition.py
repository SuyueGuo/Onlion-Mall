# Generated by Django 2.2.1 on 2019-05-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='edition',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
