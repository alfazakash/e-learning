# Generated by Django 4.1.4 on 2023-07-15 14:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                (
                    "description",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(500)]
                    ),
                ),
                ("thumb_nail", models.ImageField(null=True, upload_to="thumb_nails")),
                ("created_on", models.DateField(auto_now=True)),
                ("last_updated_on", models.DateField(auto_now=True)),
                ("price", models.FloatField()),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
