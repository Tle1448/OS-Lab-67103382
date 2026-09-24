import os
import time


def create_small_files():
    os.makedirs("small_files", exist_ok=True)

    for i in range(1000):
        with open(f"small_files/data_{i}.txt", "w") as f:
            f.write("AI training data\n")


def read_small_files():
    start = time.perf_counter()

    for i in range(1000):
        with open(f"small_files/data_{i}.txt", "r") as f:
            f.read()

    end = time.perf_counter()
    return end - start


def create_large_file():
    with open("large_dataset.txt", "w") as f:
        for i in range(1000):
            f.write("AI training data\n")


def read_large_file():
    start = time.perf_counter()

    with open("large_dataset.txt", "r") as f:
        f.read()

    end = time.perf_counter()
    return end - start


def main():
    print("--- AI Dataset I/O Benchmark ---")

    create_small_files()
    create_large_file()

    small_time = read_small_files()
    large_time = read_large_file()

    print(f"1000 Small Files Read Time: {small_time:.6f} seconds")
    print(f"1 Large File Read Time: {large_time:.6f} seconds")


if __name__ == "__main__":
    main()
