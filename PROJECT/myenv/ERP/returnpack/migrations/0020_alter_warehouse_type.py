# Generated by Django 5.0.6 on 2024-05-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0019_alter_packaging_capacity_alter_packaging_dimensions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='type',
            field=models.CharField(default='default value', max_length=10),
        ),
    ]
