from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.data_access.car_owner import CarOwnerRepository


class CarOwnerTest(TestCase):

    def setUp(self):
        user = {'username': 'teste', 'password': 'testando123'}
        self.api_client = APIClient()
        self.car_owner_repo = CarOwnerRepository()

        self.api_client.post('/api/user/', user)
        response = self.api_client.post('/api/login/', user, format='json')
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

        self.car_owner = {"name": "João"}
    
    def test_create_car_owner(self):
        """
        POST - Cria um dono de carro
        """
        response = self.api_client.post('/api/car-owner/', self.car_owner, format='json')

        # Verifico:
        # - Se o status é 201
        # - Se o dono de carro está na base de dados
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], self.car_owner_repo.get({'cd_car_owner': response.data["message"]}).cd_car_owner)
    
    def test_list_car_owner(self):
        """
        GET - Lista todos os donos de carros
        """
        response_post = self.api_client.post('/api/car-owner/', self.car_owner, format='json')
        response_get = self.api_client.get('/api/car-owner/', format='json')

        # Verifico:
        # - Se o status é 201
        # - Se o dono de carro está na base de dados
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_post.data["message"], self.car_owner_repo.get({'cd_car_owner': response_post.data["message"]}).cd_car_owner)

        # Verifico:
        # - Se o status é 200
        # - Se a quantidade de donos de carros retornada é igual a quantidade registrada na base
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_get.data), len(self.car_owner_repo.list()))
    
    def test_retrieve_car_owner(self):
        """
        GET - Retorna um dono de carro específico
        """
        response_post = self.api_client.post('/api/car-owner/', self.car_owner, format='json')
        response_get = self.api_client.get('/api/car-owner/' + str(response_post.data['message']) + '/', format='json')

        # Verifico:
        # - Se o status é 201
        # - Se o dono de carro está na base de dados
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_post.data["message"], self.car_owner_repo.get({'cd_car_owner': response_post.data["message"]}).cd_car_owner)

        # Verifico:
        # - Se o status é 200
        # - Se a quantidade de donos de carros retornada é igual a quantidade registrada na base
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.data['car_owner']['cd_car_owner'], 
                        str(self.car_owner_repo.get({'cd_car_owner':response_post.data['message']}).cd_car_owner))



