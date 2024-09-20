def merge_sort(arr):
    """
    Merge Sort Algorithm
    Time Complexity: O(n log n) for all cases
    Space Complexity: O(n)
    
    This algorithm divides the input array into two halves, recursively sorts them, 
    and then merges the two sorted halves.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted arrays."""
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr)
    sorted_arr = merge_sort(test_arr)
    print("Sorted array:", sorted_arr)
