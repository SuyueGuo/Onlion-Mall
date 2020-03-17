# Generated by Django 2.2.1 on 2019-05-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('account', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('telephone', models.DecimalField(decimal_places=0, max_digits=11)),
                ('credit', models.IntegerField(default=0)),
            ],
        ),
    ]
