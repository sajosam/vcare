# Generated by Django 4.0.4 on 2022-05-27 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='age',
        ),
        migrations.RemoveField(
            model_name='account',
            name='district',
        ),
        migrations.RemoveField(
            model_name='account',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='account',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='account',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='account',
            name='state',
        ),
    ]
