# Generated by Django 4.2.6 on 2023-10-11 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_age_alter_student_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
