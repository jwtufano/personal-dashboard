# Generated by Django 3.0.5 on 2020-04-27 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_auto_20200427_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='task_created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 9, 35, 50, 797726)),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 9, 35, 50, 797750)),
        ),
    ]
