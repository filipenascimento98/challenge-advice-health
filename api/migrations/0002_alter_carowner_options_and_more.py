# Generated by Django 4.1.2 on 2022-10-15 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="carowner",
            options={"verbose_name": "Car Owner", "verbose_name_plural": "Car Owners"},
        ),
        migrations.RenameField(
            model_name="car",
            old_name="cd_carowner",
            new_name="cd_car_owner",
        ),
        migrations.RenameField(
            model_name="carowner",
            old_name="cd_carowner",
            new_name="cd_car_owner",
        ),
    ]