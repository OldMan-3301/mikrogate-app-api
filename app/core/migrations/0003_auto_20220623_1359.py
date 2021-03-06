# Generated by Django 3.2.13 on 2022-06-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220623_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='customerDevices',
        ),
        migrations.AddField(
            model_name='contract',
            name='customerDevices',
            field=models.ManyToManyField(blank=True, to='core.CustomerDevice'),
        ),
        migrations.RemoveField(
            model_name='contract',
            name='packages',
        ),
        migrations.AddField(
            model_name='contract',
            name='packages',
            field=models.ManyToManyField(blank=True, to='core.Package'),
        ),
    ]
