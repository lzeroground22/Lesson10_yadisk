import requests


def adr_parser(file_path):
    """Функция получает имя файла из пути к нему"""
    # adr = file_path
    adr_split = file_path.replace("\\", " ")
    adr_list = adr_split.split()
    # filename = adr_list[-1]
    return adr_list[-1]


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        """Получаем ссылку для загрузки файла на Я.Диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'owerwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        """Метод загруджает файл file_path на Я.Диск"""
        href = self.get_upload_link(disk_file_path=file_path).get('href', '')
        filename = f"'{adr_parser(file_path)}'"
        print(filename)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return "Success"


if __name__ == '__main__':
    uploader = YaUploader('AQAAAAA36m8ZAADLW6XIsrMVfk9ImIKjJD3zTy0')
    result = uploader.upload("D:\Python\Lesson10_yadisk\Disk_file.txt")

    # yandex_disk = YandexDisk(token=TOKEN)
    # print(yandex_disk.get_upload_link('/Disk_file.txt'))
    # print(yandex_disk.get_file_list())
    # yandex_disk.upload_file_to_disk('Disk_file.txt', 'D:\Python\Disk_file.txt')

# from ya_disk import YandexDisk
# TOKEN = 'AQAAAAA36m8ZAADLW6XIsrMVfk9ImIKjJD3zTy0'
