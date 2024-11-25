import numpy as np
import os


def load_matrix(file_path):
    """Загрузка матрицы из файла."""
    return np.load(file_path)


def filter_matrix(matrix, threshold):
    """Отбор значений, превышающих порог, и создание массивов индексов и значений."""
    indices = np.argwhere(matrix > threshold)  # Индексы элементов
    values = matrix[matrix > threshold]  # Значения элементов

    return indices, values


def save_arrays_to_npz(file_path, indices, values):
    """Сохранение массивов в файл формата npz."""
    np.savez(file_path, indices=indices, values=values)


def save_arrays_to_npz_compressed(file_path, indices, values):
    """Сохранение массивов в сжатый файл формата npz."""
    np.savez_compressed(file_path, indices=indices, values=values)


def main():
    # Путь к файлам
    matrix_file_path = "D:/data_lab2/data/second_task.npy"
    npz_file_path = "D:/data_lab2/second_task/filtered_data.npz"
    npz_compressed_file_path = "D:/data_lab2/second_task/filtered_data_compressed.npz"

    # Загрузка матрицы
    matrix = load_matrix(matrix_file_path)

    # Пороговое значение
    threshold = 564  # Установите значение порога

    # Фильтрация матрицы
    indices, values = filter_matrix(matrix, threshold)

    # Сохранение в npz
    save_arrays_to_npz(npz_file_path, indices, values)
    save_arrays_to_npz_compressed(npz_compressed_file_path, indices, values)

    # Сравнение размеров файлов
    original_size = os.path.getsize(npz_file_path)
    compressed_size = os.path.getsize(npz_compressed_file_path)

    print(f"Размер файла без сжатия: {original_size} байт")
    print(f"Размер файла с сжатием: {compressed_size} байт")


if __name__ == "__main__":
    main()
