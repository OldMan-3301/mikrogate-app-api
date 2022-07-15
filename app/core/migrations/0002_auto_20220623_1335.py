# Generated by Django 3.2.13 on 2022-06-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='customerDevices',
        ),
        migrations.AddField(
            model_name='contract',
            name='customerDevices',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='contract',
            name='packages',
        ),
        migrations.AddField(
            model_name='contract',
            name='packages',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
