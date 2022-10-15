class RepositoryBase:
    def __init__(self, model):
        self.model = model
    
    def create(self, obj):
        '''
        Realiza a inserção de um model na base de dados
        Args:
        - obj: Dicionário com os campos do model
        Returns:
        - obj: Instância do objeto(model) criado
        '''
        return self.model(**obj)
        
    def save(self, obj):
        '''
        Realiza a inserção de um model na base de dados
        Args:
        - obj: Objeto(model) criado porém ainda não salvo
        '''
        obj.save()
    
    def get(self, query_params={}, select_related=[]):
        '''
        Retorna um único objeto com base nos parâmetros definidos:
        Args:
            - query_params: Dict com os valores referentes a filtragem
            da consulta no ORM. Utiliza-se da seguinte forma: {field:value}.
            - select_related: lista de strings com os campos a serem chamados
            no select related da consulta.
        Returns:
            - obj: Objeto Cliente.
        '''
        return self.model.objects.select_related(*select_related).get(**query_params)

    def list(self, query_params={}, order_by=[], select_related=[]):
        '''
        Realiza a listagem de dados.
            Args:
            - query_params: Dict com todos os valores, campo:valor,
            para serem levados em consideração para filtragem da 
            seleção.
            - order_by: Lista contendo strings com os campos a serem
            considerados para ordenação na listagem.
            - select_related: lista de strings com os campos a serem chamados
            no select related da consulta.
            Returns:
            - Lista de objetos.
        '''
        return self.model.objects.select_related(*select_related).filter(**query_params).order_by(*order_by)