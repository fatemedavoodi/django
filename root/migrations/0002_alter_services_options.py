# Generated by Django 4.2.3 on 2023-07-17 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['-created_date']},
        ),
    ]
