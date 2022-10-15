from django.core.exceptions import ObjectDoesNotExist


class DomainBase:
    def __init__(self, repository):
        self.repository = repository
    
    def create(self, data):
        try:
            ret = self.repository.create(data)
            self.repository.save(ret)
        except Exception as e:
            return {"message": False, "status": 400}
        
        return {"message": True, "status": 201}
    
    def list(self):
        try:
            ret = self.repository.list()
        except ObjectDoesNotExist as e:
            return {"message": "Objeto não encontrado", "status": 404}
        
        return {"message": ret, "status": 200}