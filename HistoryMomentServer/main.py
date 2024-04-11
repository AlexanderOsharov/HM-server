import io
import json
import firebase_admin
from firebase_admin import credentials, db


from download import download_and_extract_archive, process_json_files

url = "https://opendata.mkrf.ru/opendata/7705851331-egrkn/data-51-structure-6.json.zip?e={%22attachment%22:true}"

download_and_extract_archive(url)
data = process_json_files("temp")

with io.open("moscow_objects.json", "w", encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)


cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://historymomentdatabase-default-rtdb.firebaseio.com/"})

ref = db.reference("/objects")

with io.open("moscow_objects.json", "r", encoding='utf-8') as file:
    json_data = json.load(file)
    ref.set(json_data)
