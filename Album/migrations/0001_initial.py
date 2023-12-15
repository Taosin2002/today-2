# Generated by Django 4.2.7 on 2023-12-13 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Name', models.CharField(max_length=50)),
                ('Album_Release_Date', models.DateField()),
                ('Rating', models.FloatField(default=1)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musician.musici')),
            ],
        ),
    ]
