# Generated by Django 4.1.2 on 2022-10-15 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_car_cd_car_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="cd_car_owner",
            new_name="owner",
        ),
    ]