import pandas as pd
import json
import os

# Загрузка набора данных
file_path = "D:\\data_lab2\\data\\Electric_Vehicle_Population_Data.csv"
data = pd.read_csv(file_path)

# Проверка имен столбцов
print("Column names before cleaning:")
print(data.columns.tolist())

# Очистка имен столбцов от лишних пробелов
data.columns = data.columns.str.strip()

# Проверка имен столбцов после очистки
print("Column names after cleaning:")
print(data.columns.tolist())

# Отбор полей для дальнейшей работы
selected_columns = [
    "VIN (1-10)",
    "County",
    "City",
    "State",
    "Model Year",
    "Make",
    "Model",
    "Electric Range",
    "Base MSRP",
]
data_selected = data[selected_columns]

# Рассчет характеристик для числовых данных
numerical_stats = {
    "Electric Range": {
        "max": int(data_selected["Electric Range"].max()),
        "min": int(data_selected["Electric Range"].min()),
        "mean": float(data_selected["Electric Range"].mean()),
        "sum": int(data_selected["Electric Range"].sum()),
        "std": float(data_selected["Electric Range"].std()),
    },
    "Base MSRP": {
        "max": int(data_selected["Base MSRP"].max()),
        "min": int(data_selected["Base MSRP"].min()),
        "mean": float(data_selected["Base MSRP"].mean()),
        "sum": int(data_selected["Base MSRP"].sum()),
        "std": float(data_selected["Base MSRP"].std()),
    },
}

# Рассчет частоты встречаемости для текстовых данных
textual_counts = {
    "Make": data_selected["Make"].value_counts().to_dict(),
    "County": data_selected["County"].value_counts().to_dict(),
    "City": data_selected["City"].value_counts().to_dict(),
    "State": data_selected["State"].value_counts().to_dict(),
    "Model Year": data_selected["Model Year"].value_counts().to_dict(),
}

# Сохранение расчетов в JSON
results = {"numerical_stats": numerical_stats, "textual_counts": textual_counts}

with open("results.json", "w") as json_file:
    json.dump(results, json_file)

# Сохранение набора данных в разных форматах
data_selected.to_csv("Electric_Vehicle_Population_Data.csv", index=False)
data_selected.to_json(
    "Electric_Vehicle_Population_Data.json", orient="records", lines=True
)
data_selected.to_pickle("Electric_Vehicle_Population_Data.pkl")

# Сравнение размеров полученных файлов
file_sizes = {
    "csv": os.path.getsize("Electric_Vehicle_Population_Data.csv"),
    "json": os.path.getsize("Electric_Vehicle_Population_Data.json"),
    "pkl": os.path.getsize("Electric_Vehicle_Population_Data.pkl"),
}

print("Размер файлов в байтах:")
for format_type, size in file_sizes.items():
    print(f"{format_type}: {size} байт")
