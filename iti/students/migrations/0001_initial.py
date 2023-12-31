# Generated by Django 4.2.6 on 2023-10-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('grade', models.IntegerField(default=100)),
                ('age', models.IntegerField(default=10)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'female')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
