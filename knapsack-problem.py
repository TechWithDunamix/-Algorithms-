def knapsack(values, weights, capacity):
    """
    0/1 Knapsack Problem using Dynamic Programming
    Time Complexity: O(n*W) where n is the number of items and W is the capacity
    Space Complexity: O(n*W)
    
    This algorithm solves the 0/1 Knapsack problem, where given a set of items, 
    each with a weight and a value, we determine the number of each item to include 
    in a collection so that the total weight is less than or equal to a given limit 
    and the total value is as large as possible.
    """
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Reconstruct the solution
    w = capacity
    n = len(values)
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], selected_items[::-1]

# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    max_value, selected_items = knapsack(values, weights, capacity)
    print(f"Maximum value: {max_value}")
    print(f"Selected items (index): {selected_items}")
    print(f"Selected items (value, weight):")
    for i in selected_items:
        print(f"({values[i]}, {weights[i]})")
