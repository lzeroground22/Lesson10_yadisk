# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загруджает файл file_path на яндекс диск"""
#         # Тут ваша логика
#
#         return 'Вернуть ответ об успешной загрузке'
#
#
# if __name__ == '__main__':
#     uploader = YaUploader('AQAAAAA36m8ZAADLW6XIsrMVfk9ImIKjJD3zTy0')
#     result = uploader.upload('D:\Python\Lesson10_yadisk\Disk_file.txt')

adr = 'D:\Python\Lesson10_yadisk\Disk_file.txt'
adr_split = adr.replace("\\"," ")
adr_list = adr_split.split()
print(adr_list[-1])

# for symbol in adr_split:
#     print(symbol)