# Generated by Django 3.2.4 on 2021-08-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
