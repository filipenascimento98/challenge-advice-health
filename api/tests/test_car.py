from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.data_access.car import CarRepository


class CarTest(TestCase):

    def setUp(self):
        user = {'username': 'teste', 'password': 'testando123'}
        self.api_client = APIClient()
        self.car_repo = CarRepository()

        self.api_client.post('/api/user/', user)
        response = self.api_client.post('/api/login/', user, format='json')
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

        car_owner = {"name": "João"}
        car_owner_id = self.api_client.post('/api/car-owner/', car_owner)

        self.car_obj = {'owner': car_owner_id.data['message'], 'color': 'Yellow', 'model': 'Sedan'}
    
    def test_create_car(self):
        """
        POST - Cria um carro
        """
        response = self.api_client.post('/api/car/', self.car_obj, format='json')

        # Verifico:
        # - Se o status é 201
        # - Se o carro está na base de dados
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], self.car_repo.get({'cd_car': response.data["message"]}).cd_car)
    
    def test_create_car_above_limit(self):
        """
        POST - Tenta criar mais de três carros para o mesmo dono.
        """
        response_first_car = self.api_client.post('/api/car/', self.car_obj, format='json')
        response_second_car = self.api_client.post('/api/car/', self.car_obj, format='json')
        response_third_car = self.api_client.post('/api/car/', self.car_obj, format='json')
        response_fourth_car = self.api_client.post('/api/car/', self.car_obj, format='json')

        # Verifico:
        # - Se o status dos três primeiro carros é 201
        # - Se o status do quarto carro é 400 o que indica que excedeu o limite permitido de carros por pessoa.
        # - Se a mensagem retornada na criação do quarto carro é "Não é possível ter mais de 3 carros."
        self.assertEqual(response_first_car.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_second_car.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_third_car.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_fourth_car.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_fourth_car.data['message'], "Não é possível ter mais de 3 carros.")
    
    def test_create_car_with_not_allowed_color_and_model(self):
        """
        POST - Tenta criar um carro com uma cor e um modelo não permitido.
        """
        self.car_obj['color'] = "Black"
        response = self.api_client.post('/api/car/', self.car_obj, format='json')

        # Verifico:
        # - Se o status da response com a cor "Black" é 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.car_obj['model'] = "Pick-Up"
        response = self.api_client.post('/api/car/', self.car_obj, format='json')

        # Verifico:
        # - Se o status da response com o modelo "Pick-Up" é 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_car(self):
        """
        GET - Lista todos carros
        """
        response_post = self.api_client.post('/api/car/', self.car_obj, format='json')
        response_get = self.api_client.get('/api/car/', format='json')

        # Verifico:
        # - Se o status é 201
        # - Se o carro está na base de dados
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_post.data["message"], self.car_repo.get({'cd_car': response_post.data["message"]}).cd_car)

        # Verifico:
        # - Se o status é 200
        # - Se a quantidade de carros retornada é igual a quantidade registrada na base
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_get.data), len(self.car_repo.list()))
    
    def test_retrieve_car(self):
        """
        GET - Retorna um carro específico
        """
        response_post = self.api_client.post('/api/car/', self.car_obj, format='json')
        response_get = self.api_client.get('/api/car/' + str(response_post.data['message']) + '/', format='json')

        # Verifico:
        # - Se o status é 201
        # - Se o carro está na base de dados
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_post.data["message"], self.car_repo.get({'cd_car': response_post.data["message"]}).cd_car)

        # Verifico:
        # - Se o status é 201
        # - Se o carro recuperado está na base
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.data['car']['cd_car'],
                         str(self.car_repo.get({'cd_car': response_post.data["message"]}).cd_car))
    


