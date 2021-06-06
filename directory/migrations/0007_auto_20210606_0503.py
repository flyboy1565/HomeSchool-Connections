# Generated by Django 3.2.3 on 2021-06-06 05:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_alter_child_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentcontact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 6, 6, 5, 3, 30, 985431, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parentcontact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
