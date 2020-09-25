# Generated by Django 2.2 on 2020-07-08 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag', '0009_auto_20200708_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='spamtweets',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spamtweets',
            name='hashtag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hashtag.Hashtag'),
        ),
    ]
