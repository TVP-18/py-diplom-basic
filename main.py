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


def show_help():
    help_inf = """
        Программа для резервного копирования фотографий с профиля (аватарок) пользователя из VK на Яндекс.Диск.
        Для работы программы необходимы токены для VK и Яндекс.Диска.
        Укажите ID пользователя VK и количество фотографий для сохранения на Яндекс.Диск 
    """
    print(help_inf)


# информация о программе
show_help()

# входные данные
token_vk = input('Введите токен для VK: ')
token_yd = input('Введите токен для Яндекс.Диск: ')
vk_id = input_int('Введите ID пользователя VK (если не указан, определяется по токену): ')
count_save = input_int('Введите количество файлов для сохранения на Яндекс.Диск (если не указано,то 5 файлов): ', 5)

# with open('token.txt') as file:
#      token_vk = file.readline().strip()
#      token_yd = file.readline().strip()
# vk_id = 1#650124345 #552934290

my_vk = Vk(token_vk, '5.130')
my_ya_disk = YandexDisk(token_yd)

# читаем фотографии пользователя из VK
my_photos = my_vk.read_photos(vk_id)

# сохраняем фотографии на Яндекс.Диск
result = my_ya_disk.save_photos(my_photos, count_save)





