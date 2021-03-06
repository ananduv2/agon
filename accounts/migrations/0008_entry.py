# Generated by Django 4.0 on 2021-12-12 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_event_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1500)),
                ('status', models.CharField(choices=[('2', 'Pending'), ('1', 'Approved'), ('3', 'Rejected')], default='Pending', max_length=150)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.event')),
                ('student', models.ForeignKey(blank=True, limit_choices_to={'type': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
