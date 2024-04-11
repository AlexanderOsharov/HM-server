import json
import io
import os
import random

from bs4 import BeautifulSoup
import requests
import time
from pdf_test import get_description

def create_json_with_all_fields():
    flag = True
    database = []

    for i in range(1, 17):
        with io.open(f"temp/{i}.json", "r", encoding="utf-8") as file:
            f = json.load(file)
            try:
                for obj in f:
                    print(obj)
                    if obj["data"]["general"]["region"]["id"] == '77':
                        if "address" in obj["data"]["general"]:
                            if "mapPosition" in obj["data"]["general"]["address"] is not None:
                                if "type" in obj["data"]["general"]["address"]["mapPosition"]:
                                    if obj["data"]["general"]["address"]["mapPosition"]["type"] == "MultiPoint":
                                        database.append(obj)
            except:
                print("error")

    print(len(database))
    with io.open("all_fields.json", "w", encoding='utf-8') as file:
        json.dump(database, file, ensure_ascii=False)
