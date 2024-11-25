import json
import msgpack
import os


def load_json(file_path):
    """Загрузка JSON файла."""
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def aggregate_product_info(data):
    """Агрегирование информации о товарах."""
    aggregated_data = {}

    # Проход по каждому товару
    for product in data:
        name = product["name"]
        price = product["price"]
        category = product["category"]

        if name not in aggregated_data:
            aggregated_data[name] = {
                "name": name,
                "category": category,
                "prices": [],
                "quantities": [],
            }

        aggregated_data[name]["prices"].append(price)
        aggregated_data[name]["quantities"].append(product["quantity"])

    # Подсчет средней, максимальной и минимальной цены
    result = []
    for name, info in aggregated_data.items():
        average_price = sum(info["prices"]) / len(info["prices"])
        max_price = max(info["prices"])
        min_price = min(info["prices"])
        total_quantity = sum(info["quantities"])

        result.append(
            {
                "name": name,
                "category": info["category"],
                "average_price": average_price,
                "max_price": max_price,
                "min_price": min_price,
                "quantity": total_quantity,
            }
        )

    return result


def save_to_json(file_path, data):
    """Сохранение данных в формат JSON с правильной кодировкой."""
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def save_to_msgpack(file_path, data):
    """Сохранение данных в формат Msgpack."""
    with open(file_path, "wb") as msgpack_file:
        msgpack.pack(data, msgpack_file)


def main():
    # Путь к файлам
    json_file_path = "D:/data_lab2/data/third_task.json"
    aggregated_json_file_path = "D:/data_lab2/third_task/aggregated_data.json"
    aggregated_msgpack_file_path = "D:/data_lab2/third_task/aggregated_data.msgpack"

    # Загрузка данных из JSON
    data = load_json(json_file_path)

    # Агрегирование информации
    aggregated_data = aggregate_product_info(data)

    # Сохранение в JSON
    save_to_json(aggregated_json_file_path, aggregated_data)

    # Сохранение в Msgpack
    save_to_msgpack(aggregated_msgpack_file_path, aggregated_data)

    # Сравнение размеров файлов
    json_size = os.path.getsize(aggregated_json_file_path)
    msgpack_size = os.path.getsize(aggregated_msgpack_file_path)

    print(f"Размер файла JSON: {json_size} байт")
    print(f"Размер файла Msgpack: {msgpack_size} байт")


if __name__ == "__main__":
    main()
