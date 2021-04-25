import requests
from datetime import datetime
from pprint import pprint


class Vk:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def get_name(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        url = self.url + 'users.get'
        params = {
            'user_ids': user_id
        }
        response = requests.get(url, params={**self.params, **params}).json()
        return f"{response['response'][0]['first_name']} {response['response'][0]['last_name']}"

    def get_photos(self, user_id=None, count=50):
        if user_id is None:
            user_id = self.owner_id
        url = self.url + 'photos.get'
        params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'extended': 1,
            'count': count
        }
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def max_quality(self, sizes_list):
        typ = 'a'
        max_el = {}
        for el in sizes_list:
            if el['type'] > typ:
                typ = el['type']
                max_el = el
        return max_el

    def read_photos(self, user_id=None, count=50):
        if user_id is None:
            user_id = self.owner_id

        print(f'Получаем фотографии из VK для профиля {self.get_name(user_id)} (ID={user_id})')

        photos = []
        vk_photos = self.get_photos(user_id, count)
        for item in vk_photos['response']['items']:
            quality_photo = self.max_quality(item['sizes'])

            photos.append({
                'date': datetime.utcfromtimestamp(item['date']).strftime('%Y%m%d_%H%M%S'),
                'likes': item['likes']['count'],
                'url': quality_photo['url'],
                'size': quality_photo['type']
            })
        print(f'Найдено фотографий: {len(photos)}')
        return photos
