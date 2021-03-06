# Generated by Django 3.2.7 on 2021-12-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('roll', models.CharField(max_length=9)),
                ('branch', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
    ]
