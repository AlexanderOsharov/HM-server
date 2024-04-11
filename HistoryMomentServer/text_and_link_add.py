import random
import time
from bs4 import BeautifulSoup
import requests

from ai_new_old_version import get_subs_text
from pdf_test import get_description

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def clean_json_and_add_text(json_data):
    new_file = []
    errors = []
    for o in json_data:
        objecto = o["data"]["general"]
        if "photo" not in objecto or "mapPosition" not in objecto["address"]:
            continue
        if objecto["address"] is None or objecto["photo"] is None or \
                objecto["name"] is None:
            continue
        else:
            query = (objecto["address"]["fullAddress"] + " акт государственной историко культурной экспертизы")
            print(query)

            url = f"https://ya.ru/search/?text={query}"
            time.sleep(random.randint(3, 6))
            response = requests.get(url, headers=headers)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            links = soup.find_all("a", href=True)

            pdf_url = None

            try:
                for link in links:
                    if link["href"].startswith("https://www.mos.ru/upload/documents/files"):
                        pdf_url = link.get("href")
                        break
                if pdf_url:
                    new_obj = {"name": objecto["name"], "address": objecto["address"], "hash": o["hash"],
                               "photo": objecto["photo"], "link": pdf_url, "description": get_subs_text(get_description(pdf_url))}
                    print(new_obj)
                    new_file.append(new_obj)

                else:
                    new_obj = {"name": objecto["name"], "address": objecto["address"], "hash": o["hash"],
                               "photo": objecto["photo"],
                               "description": "Не получилось достать текст",
                               "link": pdf_url}
                    print(new_obj)
                    errors.append(new_obj)
            except Exception as e:
                print(e)

    print(len(new_file), " - good")
    print(len(errors), " - errors")
    return new_file
    # with io.open("moscow_links.json", "w", encoding='utf-8') as file:
    #     json.dump(new_file, file, ensure_ascii=False)
    #
    # with io.open("moscow_links_errors.json", "w", encoding='utf-8') as file:
    #     json.dump(errors, file, ensure_ascii=False)
