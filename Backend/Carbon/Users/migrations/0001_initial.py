# Generated by Django 4.1.7 on 2023-02-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=150, null=True)),
                ("email", models.CharField(max_length=150, null=True)),
                ("password", models.CharField(max_length=150, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("staff", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
    ]
