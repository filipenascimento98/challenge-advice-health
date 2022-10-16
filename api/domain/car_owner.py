from api.domain.base import DomainBase
from api.data_access.car_owner import CarOwnerRepository

class CarOwnerDomain(DomainBase):
    def __init__(self):
        super().__init__(CarOwnerRepository())
