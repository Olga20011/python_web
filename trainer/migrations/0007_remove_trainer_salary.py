# Generated by Django 3.2.4 on 2021-08-19 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0006_auto_20210819_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='salary',
        ),
    ]
