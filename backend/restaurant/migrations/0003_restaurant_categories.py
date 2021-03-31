# Generated by Django 3.0.3 on 2021-03-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('restaurant', '0002_restaurant_restaurant_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(related_name='restaurants', to='category.Category'),
        ),
    ]
