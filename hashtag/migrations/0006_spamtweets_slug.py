# Generated by Django 2.2 on 2020-07-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag', '0005_auto_20200708_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='spamtweets',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
