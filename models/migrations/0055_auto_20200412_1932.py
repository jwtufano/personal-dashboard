# Generated by Django 3.0.5 on 2020-04-13 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0054_auto_20200412_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='task_created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 19, 32, 29, 751497)),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 19, 32, 29, 751602)),
        ),
    ]