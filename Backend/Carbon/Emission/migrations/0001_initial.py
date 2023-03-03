# Generated by Django 4.1.7 on 2023-03-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emission",
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
                ("transportation", models.CharField(max_length=150, null=True)),
                ("enery_consumption", models.CharField(max_length=150, null=True)),
                ("food_consumption", models.CharField(max_length=150, null=True)),
                ("total", models.CharField(max_length=150, null=True)),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
    ]
