# Generated by Django 4.1.4 on 2023-07-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devedu", "0003_coursecontent"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursecontent",
            name="title",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="title",
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]