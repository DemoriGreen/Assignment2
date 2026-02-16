import random
import time


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search_iterative(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(data, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, right)
    else:
        return binary_search_recursive(data, target, left, mid - 1)


def test_search_correctness():
    data_unsorted = [5, 3, 9, 1, 7]
    data_sorted = sorted(data_unsorted)

    print("Test 1:", linear_search(data_unsorted, 9) != -1)
    print("Test 2:", linear_search(data_unsorted, 100) == -1)
    print("Test 3:", binary_search_iterative(data_sorted, 7) != -1)
    print("Test 4:", binary_search_recursive(data_sorted, 7, 0, len(data_sorted)-1) != -1)


def benchmark_search(algorithm, data, targets, needs_sort=False):
    if needs_sort:
        start_sort = time.time()
        data = sorted(data)
        sort_time = time.time() - start_sort
    else:
        sort_time = 0

    start = time.time()

    for target in targets:
        if algorithm == "linear":
            linear_search(data, target)
        elif algorithm == "binary_iter":
            binary_search_iterative(data, target)
        elif algorithm == "binary_rec":
            binary_search_recursive(data, target, 0, len(data) - 1)

    total_time = time.time() - start
    return total_time + sort_time


def benchmark_all():
    print("\nBENCHMARK RESULTS\n")

    customer_ids = random.sample(range(1_000_000), 100_000)
    product_catalog = sorted(random.sample(range(1_000_000), 50_000))
    config_settings = random.sample(range(10_000), 500)
    dictionary_words = sorted(random.sample(range(100_000), 10_000))

    datasets = [
        ("Customer IDs (100K unsorted)", customer_ids, True),
        ("Product Catalog (50K sorted)", product_catalog, False),
        ("Config Settings (500 unsorted)", config_settings, True),
        ("Dictionary Words (10K sorted)", dictionary_words, False)
    ]

    for name, data, needs_sort in datasets:
        targets = random.sample(data, 100)

        print(name)

        linear_time = benchmark_search("linear", data, targets)
        print("  Linear:", round(linear_time, 5), "seconds")

        binary_iter_time = benchmark_search("binary_iter", data, targets, needs_sort)
        print("  Binary Iterative:", round(binary_iter_time, 5), "seconds")

        binary_rec_time = benchmark_search("binary_rec", data, targets, needs_sort)
        print("  Binary Recursive:", round(binary_rec_time, 5), "seconds")

        print()


def analyze_preprocessing():
    print("\nPREPROCESSING ANALYSIS\n")

    data = random.sample(range(1_000_000), 100_000)

    start_sort = time.time()
    sorted_data = sorted(data)
    sort_time = time.time() - start_sort

    print("Sorting time:", round(sort_time, 5), "seconds")

    for searches in [1, 5, 10, 20, 50, 100]:
        targets = random.sample(data, searches)

        start_linear = time.time()
        for t in targets:
            linear_search(data, t)
        linear_time = time.time() - start_linear

        start_binary = time.time()
        for t in targets:
            binary_search_iterative(sorted_data, t)
        binary_time = time.time() - start_binary

        total_binary = sort_time + binary_time

        print(f"{searches} searches -> "
              f"Linear: {round(linear_time,5)}s | "
              f"Sort+Binary: {round(total_binary,5)}s")


if __name__ == "__main__":
    test_search_correctness()
    benchmark_all()
    analyze_preprocessing()

git add .
git commit -m "Completed recursive file system analysis"
git push
