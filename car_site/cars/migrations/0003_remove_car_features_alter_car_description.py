# Generated by Django 4.1.1 on 2023-01-10 18:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_doors_alter_car_fuel_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
