# Generated by Django 3.2.23 on 2024-02-03 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='register_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
