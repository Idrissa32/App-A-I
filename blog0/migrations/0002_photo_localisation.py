# Generated by Django 4.1.1 on 2022-11-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog0', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='localisation',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
