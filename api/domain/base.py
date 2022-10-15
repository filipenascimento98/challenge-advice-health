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