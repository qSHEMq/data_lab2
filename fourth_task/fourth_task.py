import pickle
import json


def load_products(file_path):
    """Загрузка данных о товарах из файла формата pkl."""
    with open(file_path, "rb") as file:
        products = pickle.load(file)
    return products


def load_updates(file_path):
    """Загрузка данных об обновлениях цен из файла формата json."""
    with open(file_path, "r", encoding="utf-8") as file:
        updates = json.load(file)
    return updates


def update_prices(products, updates):
    """Обновление цен товаров в зависимости от методов."""
    for update in updates:
        name = update["name"]
        method = update["method"]
        param = update["param"]

        # Найти товар по имени
        for product in products:
            if product["name"] == name:
                if method == "add":
                    product["price"] += param
                elif method == "sub":
                    product["price"] -= param
                elif method == "percent+":
                    product["price"] *= 1 + param
                elif method == "percent-":
                    product["price"] *= 1 - param
                break  # Выход из цикла после обновления

    return products


def save_products(file_path, products):
    """Сохранение данных о товарах в файл формата pkl."""
    with open(file_path, "wb") as file:
        pickle.dump(products, file)


def main():
    # Путь к файлам
    products_file_path = "D:/data_lab2/data/fourth_task_products.pkl"
    updates_file_path = "D:/data_lab2/data/fourth_task_updates.json"
    modified_products_file_path = "D:/data_lab2/fourth_task/modified_products.pkl"

    # Загрузка данных о товарах
    products = load_products(products_file_path)

    # Загрузка данных об обновлениях цен
    updates = load_updates(updates_file_path)

    # Обновление цен
    updated_products = update_prices(products, updates)

    # Сохранение модифицированных данных в pkl
    save_products(modified_products_file_path, updated_products)

    print("Цены успешно обновлены и сохранены.")


if __name__ == "__main__":
    main()
