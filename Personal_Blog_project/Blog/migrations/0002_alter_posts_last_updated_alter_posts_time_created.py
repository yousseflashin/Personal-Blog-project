# Generated by Django 5.0.3 on 2024-03-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
