# Generated by Django 3.2.4 on 2021-08-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=10)),
                ('duration', models.PositiveSmallIntegerField()),
                ('syllabus', models.TextField()),
            ],
        ),
    ]
