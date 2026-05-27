import json


def load_json_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json_data(data, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def append_json_record(record, path):
    data = load_json_data(path)
    data.append(record)
    save_json_data(data, path)


def get_next_id(records):
    if len(records) == 0:
        return 1

    biggest_id = max(record["id"] for record in records)
    return biggest_id + 1
