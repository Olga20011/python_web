# Generated by Django 3.2.4 on 2021-08-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0007_remove_trainer_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='profile',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
