# Generated by Django 4.1.3 on 2022-12-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0005_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('character_img', models.URLField()),
                ('main_attack', models.CharField(max_length=25, unique=True)),
                ('special_attack', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
