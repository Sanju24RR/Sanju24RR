def fractionalKnapsack(capacity, profits, weights):
    items = list(zip([p/w for p, w in zip(profits, weights)], profits, weights))
    items.sort(reverse=True)
    finalvalue = 0.0
    remaining_capacity = capacity
    for ratio, profit, weight in items:
        if weight <= remaining_capacity:
            # Take whole item
            remaining_capacity -= weight
            finalvalue += profit
        else:
            # Take fraction of item
            finalvalue += profit * remaining_capacity / weight
            break         
    return finalvalue

capacity = 50
profits = [60, 120, 120]  # Profits of items
weights = [10, 20, 30]    # Weights of items
    
max_val = fractionalKnapsack(capacity, profits, weights)
print(f"Maximum value achieved: {max_val}")