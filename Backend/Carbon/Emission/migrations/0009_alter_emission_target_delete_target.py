# Generated by Django 4.1.7 on 2023-03-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Emission", "0008_alter_emission_energyconsumption_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emission", name="target", field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(name="Target",),
    ]
