# Generated by Django 3.0.5 on 2020-04-27 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20200426_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='task_created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 3, 40, 54, 49704)),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 27, 3, 40, 54, 49727)),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='task_priority',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=1),
        ),
    ]