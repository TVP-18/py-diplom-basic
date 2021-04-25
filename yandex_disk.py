import requests
import json
import time
from tqdm import tqdm
from datetime import datetime


class YandexDisk:
    url = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_name):
        url = self.url + 'v1/disk/resources'
        params = {
            'path': folder_name
        }
        response = requests.put(url, headers=self.headers, params=params)
        # if response.status_code == 201:
        #     print(f'На Яндекс.Диск создана новая папка {folder_name}')

        return response.json()

    def load_url(self, file_path, file_name):
        url = self.url + 'v1/disk/resources/upload'
        params = {
            'url': file_path,
            'path': file_name
        }
        response = requests.post(url, headers=self.headers, params=params)

        if response.status_code == 202:  # файл успешно загружен
            return True

        return response

    def save_photos(self, photos, count=5):
        print(f'Делаем резервные копии фотографий на Яндекс.Диск')
        load_json = []

        # создаем на Яндекс.Диске новую папку для сохранения фото
        folder_name = f'backup_vk_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        self.create_folder(folder_name)

        # загружаем файлы
        for item in tqdm(photos[0:count]):
            full_name = folder_name+f"/{item['likes']}_{item['date']}.jpg"

            result = self.load_url(item['url'], full_name)

            load_json.append({'file_name': full_name, 'size': item['size'], 'status_load': result})

            time.sleep(1)

        with open('load.json', 'w') as file:
            json.dump(load_json, file, ensure_ascii=False, indent=3)

        print(f'Информация о загрузке в файле load.json')

        return load_json

