# hw_yandex_disk

**Задание 2**

import requests

class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = f'{self.host}/v1/disk/resources/upload'
        print(url, file_path)
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'
                   }
        params = {'path': file_path, 'owerwrite': True}
        resp = requests.get(url, params=params, headers=headers).json()['href']
        response = requests.put(resp, data=open(file_path, 'rb'), headers=headers)
        print(response)
        if response.status_code == 201:
            print("Done")


if __name__ == '__main__':
    path_to_file = 'backup.txt'
    token = '7777777777777777777777777777777777777777'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
