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
            query_params = {"cd_car_owner": data["cd_car_owner"]}
            car_owner = self.car_owner_repository.get(query_params=query_params)

            data["cd_car_owner"] = car_owner
        except ObjectDoesNotExist as e:
            return {"message": "Dono de carro não encontrado", "status": 404}

        try:
            ret = self.repository.create(data)
            self.repository.save(ret)
        except Exception as e:
            return {"message": False, "status": 400}
        
        return {"message": True, "status": 201}