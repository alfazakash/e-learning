# Generated by Django 4.1.4 on 2023-07-15 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devedu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(
                validators=[django.core.validators.MaxLengthValidator(500)]
            ),
        ),
    ]
