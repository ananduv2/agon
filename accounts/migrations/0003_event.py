# Generated by Django 4.0 on 2021-12-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_pic_account_profilepic_account_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('entry_date', models.DateField()),
                ('last_date', models.DateField()),
                ('details', models.TextField()),
            ],
        ),
    ]