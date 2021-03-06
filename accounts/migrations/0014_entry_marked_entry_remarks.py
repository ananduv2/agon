# Generated by Django 4.0 on 2021-12-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_liveevent_entry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='marked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='remarks',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
