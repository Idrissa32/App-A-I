# Generated by Django 4.1.1 on 2022-12-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog0', '0010_alter_photo_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commants', to='blog0.photo')),
            ],
        ),
    ]
