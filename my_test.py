import unittest
import requests

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000'

    def test_signup(self):
        data = {'username': 'test_user', 'email':'mail@gmail.com', 'password': 'test_password' }
        response = requests.post(f'{self.url}/signup', data= data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Користувач успішно зареєстрований')

    def test_login(self):
        data = {'username': 'test_user', 'password': 'test_password'}
        response = requests.post(f'{self.url}/login', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Вхід успішний')

    def test_encrypt(self):
        data = {'text': 'test_text'}
        response = requests.post(f'{self.url}/encrypt', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['encrypted_text'])

    def test_decrypt(self):
        data = {'text1': 'test_text1'}
        response = requests.post(f'{self.url}/decrypt', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['error'], 'Потрібен зашифрований текст')


if __name__ == '__main__':
    unittest.main()