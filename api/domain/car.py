from django.core.exceptions import ObjectDoesNotExist

from api.domain.base import DomainBase
from api.data_access.car import CarRepository
from api.data_access.car_owner import CarOwnerRepository


class CarDomain(DomainBase):
    def __init__(self):
        self.car_owner_repository = CarOwnerRepository()
        super().__init__(CarRepository())
    
    def create(self, data):
        try:
            query_params = {"cd_car_owner": data["owner"]}
            prefetch_related = ['car']
            car_owner = self.car_owner_repository.get_with_related(
                query_params=query_params, 
                prefetch_related=prefetch_related
            )

            data["owner"] = car_owner
        except ObjectDoesNotExist as e:
            return {"message": "Dono de carro não encontrado", "status": 404}

        if car_owner.car.count() >= 3:
            return {"message": "Não é possível ter mais de 3 carros.", "status": 400}

        ret = self.repository.create(data)
        self.repository.save(ret)

        car_owner.sales_opportunity = False
        self.car_owner_repository.update(
            car_owner,
            changed_data={"update_fields": ["sales_opportunity"]}
        )
        
        return {"message": ret.pk, "status": 201}