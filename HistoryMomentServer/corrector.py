import json
import io
import os
import time
from ai_new_old_version import get_subs_text

new_file = []
with io.open("new_ai_version_objects.json", "r", encoding='utf-8') as file:
    json_data = json.load(file)

    errors = 0
    succeed = 0

    size = len(json_data)
    for object in json_data:
        try:
            # ref = get_subs_text(object["description"])
            # if ref is not None:
            # print(ref)
            new_obj = {"name": object["name"], "address": object["address"], "hash": object["hash"],
                       "photo": object["photo"], "link": object["link"], "description": object["history_reference"]}
            new_file.append(new_obj)
            succeed += 1
            print(f" succeeded {succeed} / {size}")
            print(f" errors {errors} / {size}")
            print()
            # else:
            #     errors += 1
            #     print(f" succeeded {succeed} / {size}")
            #     print(f" errors {errors} / {size}")
            #     print()
        except:
            errors += 1
            print(f" succeeded {succeed} / {size}")
            print(f" errors {errors} / {size}")
            print()

print(len(new_file))
with io.open("version_only_historical_references.json", "w", encoding='utf-8') as file:
    json.dump(new_file, file, ensure_ascii=False)
