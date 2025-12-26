import random
import time


def merge_sort(arr):
    """
    Merge Sort algorithm implementation
    """
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    # Generate 100 random numbers between 1 and 1000
    numbers = [random.randint(1, 1000) for _ in range(100)]

    print("Original array (first 10 numbers):", numbers[:10])
    print(f"Total numbers: {len(numbers)}\n")

    # Measure sorting time
    start_time = time.time()
    sorted_numbers = merge_sort(numbers)
    end_time = time.time()

    # Calculate execution time
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

    print("Sorted array (first 10 numbers):", sorted_numbers[:10])
    print("Sorted array (last 10 numbers):", sorted_numbers[-10:])
    print(f"\nTime taken to sort: {execution_time:.4f} milliseconds")


if __name__ == "__main__":
    main()
