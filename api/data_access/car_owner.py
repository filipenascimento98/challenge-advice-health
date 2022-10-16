from api.data_access.base import RepositoryBase
from api.models import CarOwner


class CarOwnerRepository(RepositoryBase):
    def __init__(self):
        super().__init__(CarOwner)