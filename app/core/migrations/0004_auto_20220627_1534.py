# Generated by Django 3.2.13 on 2022-06-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220623_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='status',
            field=models.CharField(choices=[('done', 'Done'), ('in-progress', 'In-Progress'), ('pending', 'Pending'), ('canceled', 'Canceled'), ('expired', 'Expired')], default='pending', max_length=15),
        ),
        migrations.AddField(
            model_name='customerdevice',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
