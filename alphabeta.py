import math

# Minimax function with alpha-beta pruning
def minimax(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cut-off
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cut-off
        return best

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # leaf node values
    max_depth = 3  # log2(len(values)) = 3
    best_score = minimax(0, 0, True, values, -math.inf, math.inf, max_depth)
    print("The optimal value is:", best_score)
