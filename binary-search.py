def binary_search(arr, target):
    """
    Binary Search Algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    This algorithm works on sorted arrays. It repeatedly divides the search 
    interval in half until the target element is found or it's clear the 
    target is not in the array.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    sorted_arr = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    result = binary_search(sorted_arr, target)
    print(f"Array: {sorted_arr}")
    print(f"Searching for: {target}")
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array")
