# Generated by Django 5.2 on 2025-04-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('User_id', models.IntegerField(primary_key=True, serialize=False)),
                ('User_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Movie_name', models.CharField(max_length=100)),
                ('No_of_seats', models.IntegerField()),
            ],
        ),
    ]
