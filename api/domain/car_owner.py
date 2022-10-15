from api.domain.base import DomainBase
from api.data_access.car_owner import CarOwnerRepository

class CarOwnerDomain(DomainBase):
    def __init__(self):
        super().__init__(CarOwnerRepository())
    
    def create(self, data_car_owner):
        try:
            ret = self.repository.create(data_car_owner)
            self.repository.save(ret)
        except Exception as e:
            return {"success": False, "status": 400}
        
        return {"success": True, "status": 201}
