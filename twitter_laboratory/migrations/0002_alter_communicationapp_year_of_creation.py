# Generated by Django 4.0.4 on 2022-05-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_laboratory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationapp',
            name='year_of_creation',
            field=models.CharField(max_length=4),
        ),
    ]
