# Generated by Django 5.0.6 on 2024-05-29 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0012_remove_packaging_durabilty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagingmouvment',
            name='date',
        ),
    ]
