def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n^2) in worst and average cases, O(n) in best case
    Space Complexity: O(1)
    
    This algorithm repeatedly steps through the list, compares adjacent 
    elements and swaps them if they are in the wrong order.
    """
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_arr)
    sorted_arr = bubble_sort(test_arr)
    print("Sorted array:", sorted_arr)
