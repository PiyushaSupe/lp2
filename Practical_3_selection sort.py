def print_array(arr, min_idx, i):
    """Prints the array with brackets around the selected elements."""
    result = []
    for idx, num in enumerate(arr):
        if idx == min_idx or idx == i:
            result.append(f"[{num}]")  # Highlight selected elements
        else:
            result.append(str(num))
    print(" ".join(result))

def selection_sort(arr):
    """Performs selection sort and displays each iteration."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Print the array after swapping
        print(f"Iteration {i + 1}: ", end="")
        print_array(arr, min_idx, i)

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
