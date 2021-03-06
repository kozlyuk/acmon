# Generated by Django 3.2.1 on 2021-06-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_trip_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='event_id',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Event ID'),
        ),
        migrations.AddField(
            model_name='record',
            name='io_elements',
            field=models.JSONField(default=list, verbose_name='IO Elements'),
        ),
        migrations.AlterField(
            model_name='record',
            name='satellites',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Satelites'),
        ),
    ]
