# Generated by Django 4.2.7 on 2023-12-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Instrument_Type', models.CharField(max_length=50)),
            ],
        ),
    ]
