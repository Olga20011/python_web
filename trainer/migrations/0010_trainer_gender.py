# Generated by Django 3.2.4 on 2021-08-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0009_auto_20210826_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='gender',
            field=models.CharField(choices=[('1', 'Female'), ('2', 'Male')], max_length=10, null=True),
        ),
    ]
