def mean(numbers):
    """Compute the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    return min(modes)  # Return the smallest mode if multiple

# Example usage (remove or comment out if using as a module)
if __name__ == "__main__":
    data = [1, 2, 3, 4, 4, 5]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))