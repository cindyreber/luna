# Generated by Django 3.0.3 on 2021-03-29 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant_review', '0001_initial'),
        ('user_profile', '0002_auto_20210329_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ManyToManyField(related_name='liked_comments', to='user_profile.UserProfile')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='restaurant_review.RestaurantReview')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user_profile.UserProfile')),
            ],
        ),
    ]
