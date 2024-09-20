def quick_sort(arr):
    """
    Quick Sort Algorithm
    Time Complexity: O(n log n) average and best case, O(n^2) worst case
    Space Complexity: O(log n) average case, O(n) worst case
    
    This algorithm selects a 'pivot' element and partitions the other elements 
    into two sub-arrays, according to whether they are less than or greater than the pivot.
    The sub-arrays are then recursively sorted.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr)
    sorted_arr = quick_sort(test_arr)
    print("Sorted array:", sorted_arr)
