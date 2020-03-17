# Generated by Django 2.2.1 on 2019-05-21 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Commodity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
