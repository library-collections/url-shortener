# Generated by Django 3.1.6 on 2021-02-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
        migrations.AddField(
            model_name='url',
            name='hashed_url',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]