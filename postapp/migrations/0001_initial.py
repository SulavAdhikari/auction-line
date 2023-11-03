# Generated by Django 4.2.2 on 2023-08-20 11:04

import datetime
from django.db import migrations, models
import postapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default=None, max_length=16)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(default='Any', max_length=255)),
                ('description', models.TextField(null=True)),
                ('comp_image', models.ImageField(null=True, upload_to=postapp.models.Post.namecomFile1)),
                ('sell_location', models.CharField(default='any', max_length=128)),
                ('sold', models.BooleanField(default=False)),
                ('bidstart', models.IntegerField(default=0)),
                ('buynow', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 8, 20, 16, 49, 16, 72235))),
                ('date_end', models.DateTimeField(default=None)),
            ],
        ),
    ]
