# Generated by Django 4.0.4 on 2022-06-02 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_account_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 21, 16, 58, 692485)),
        ),
    ]
