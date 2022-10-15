from django.db import models
from uuid import uuid4


class CarOwner(models.Model):
    cd_car_owner = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField("Name", max_length=30)
    sales_opportunity = models.BooleanField("Sales Opportunity", default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Car Owner"
        verbose_name_plural = "Car Owners"

class Car(models.Model):
    cd_car = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cd_car_owner = models.ForeignKey(
        "CarOwner",
        verbose_name="Car Owner",
        related_name="car",
        on_delete=models.DO_NOTHING
    )
    color = models.CharField(
        "Color",
        max_length=10, 
        choices=[('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Gray', 'Gray')]
    )
    model = models.CharField(
        "Model",
        max_length=15, 
        choices=[('Hatch', 'Hatch'), ('Sedan', 'Sedan'), ('Convertible', 'Convertible')]
    )

    def __str__(self):
        return self.cd_car_owner.name + " - " + self.color + " - " + self.model