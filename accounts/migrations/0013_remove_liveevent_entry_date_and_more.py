# Generated by Django 4.0 on 2021-12-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_liveevent_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liveevent',
            name='entry_date',
        ),
        migrations.RemoveField(
            model_name='liveevent',
            name='last_date',
        ),
        migrations.AddField(
            model_name='liveevent',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='liveevent',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
