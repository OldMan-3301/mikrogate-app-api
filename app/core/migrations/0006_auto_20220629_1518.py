# Generated by Django 3.2.13 on 2022-06-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220629_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='dev_amnt',
            new_name='ann_amnt',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='dev_amnt_totl',
            new_name='ann_amnt_totl',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='dev_cond',
            new_name='ann_cond',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='dev_dec',
            new_name='ann_dec',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='dev_qty',
            new_name='ann_qty',
        ),
        migrations.AddField(
            model_name='contract',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='rou_amnt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='rou_amnt_totl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='rou_cond',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contract',
            name='rou_dec',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contract',
            name='rou_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
