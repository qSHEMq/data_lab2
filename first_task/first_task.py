import numpy as np
import json


def load_matrix(file_path):
    """Загрузка матрицы из файла."""
    matrix = np.load(file_path)
    return matrix


def calculate_metrics(matrix):
    """Подсчет необходимых метрик."""
    total_sum = np.sum(matrix)
    average = np.mean(matrix)

    main_diag = np.diagonal(matrix)
    sum_main_diag = np.sum(main_diag)
    average_main_diag = np.mean(main_diag)

    sec_diag = np.diagonal(np.fliplr(matrix))
    sum_sec_diag = np.sum(sec_diag)
    average_sec_diag = np.mean(sec_diag)

    max_value = np.max(matrix)
    min_value = np.min(matrix)

    results = {
        "sum": int(total_sum),
        "avr": float(average),
        "sumMD": int(sum_main_diag),
        "avrMD": float(average_main_diag),
        "sumSD": int(sum_sec_diag),
        "avrSD": float(average_sec_diag),
        "max": int(max_value),
        "min": int(min_value),
    }

    return results


def save_results_to_json(results, file_path):
    """Сохранение результатов в JSON файл."""
    with open(file_path, "w") as json_file:
        json.dump(results, json_file, indent=4)


def normalize_matrix(matrix):
    """Нормализация матрицы."""
    normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
    return normalized_matrix


def save_normalized_matrix(normalized_matrix, file_path):
    """Сохранение нормализованной матрицы в npy файл."""
    np.save(file_path, normalized_matrix)


def main():
    # Путь к файлам
    matrix_file_path = "D:/data_lab2/data/first_task.npy"
    results_file_path = "D:/data_lab2/first_task/first_task_results.json"
    normalized_matrix_file_path = "D:/data_lab2/first_task/normalized_first_task.npy"

    # Чтение матрицы
    matrix = load_matrix(matrix_file_path)

    # Подсчет метрик
    results = calculate_metrics(matrix)

    # Сохранение результатов
    save_results_to_json(results, results_file_path)

    # Нормализация матрицы
    normalized_matrix = normalize_matrix(matrix)

    # Сохранение нормализованной матрицы
    save_normalized_matrix(normalized_matrix, normalized_matrix_file_path)


if __name__ == "__main__":
    main()
