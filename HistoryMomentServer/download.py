import io
import os
import requests
import zipfile
import json
from io import BytesIO

from create_json import create_json_with_all_fields
from text_and_link_add import clean_json_and_add_text


# Функция для скачивания и извлечения архива
def download_and_extract_archive(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Скачиваем файл в память
        zip_file = BytesIO(response.content)
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall("temp")
    else:
        print("Не удалось скачать архив")


def process_json_files(directory):
    database = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with io.open(file_path, 'r', encoding='utf-8') as file:
                f = json.load(file)
                try:
                    for obj in f:
                        if obj["data"]["general"]["region"]["id"] == '77':
                            if "address" in obj["data"]["general"]:
                                if "mapPosition" in obj["data"]["general"]["address"] is not None:
                                    if "type" in obj["data"]["general"]["address"]["mapPosition"]:
                                        if obj["data"]["general"]["address"]["mapPosition"]["type"] == "Point":
                                            database.append(obj)
                except:
                    print("error")

            os.remove(file_path)
    #print(database)

    final_database = clean_json_and_add_text(database)
    return final_database


url = "https://opendata.mkrf.ru/opendata/7705851331-egrkn/data-51-structure-6.json.zip?e={%22attachment%22:true}"

if __name__ == "__main__":
    download_and_extract_archive(url)
    data = process_json_files("temp")
