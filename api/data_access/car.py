from api.data_access.base import RepositoryBase
from api.models import Car


class CarRepository(RepositoryBase):
    def __init__(self):
        super().__init__(Car)