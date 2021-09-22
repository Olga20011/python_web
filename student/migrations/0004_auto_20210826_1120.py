# Generated by Django 3.2.4 on 2021-08-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='nationalId',
            new_name='national_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='medical_report',
            field=models.FileField(null=True, upload_to='docs/'),
        ),
    ]
