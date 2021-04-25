from datetime import datetime

from vk import Vk
from yandex_disk import YandexDisk


def input_int(caption, data_default=None):
    while True:
        data = input(caption)
        if data == '':
            return data_default
        if data.isdigit():
            return int(data)
        print('Должно быть введено целое положительное число! Повторите ввод!')


# входные данные
# token_vk = input('Введите токен для VK: ')
# token_yd = input('Введите токен для Яндекс.Диск: ')
# vk_id = input_int('Введите ID пользователя VK (если не указан, определяется по токену): ')
# count_save = input_int('Введите количество файлов для сохранения на Яндекс.Диск (по умолчанию 5): ', 5)

with open('token.txt') as file:
     token_vk = file.readline().strip()
     token_yd = file.readline().strip()


vk_id = 1#650124345 #552934290
count_save = 10

my_vk = Vk(token_vk, '5.130')
my_ya_disk = YandexDisk(token_yd)

my_photos = my_vk.read_photos(vk_id)
result = my_ya_disk.save_photos(my_photos, count_save)



# with open('load_inf.json', 'w') as file:
#     json.dump(json_file, file, ensure_ascii=False, indent=3)
#




