def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    weights = dict()

    for i in range(length):
        y = weights.get(limit - weights[i])
        if y != None:
            return (i, y)
        else:
            weights[weights[i]] = i

    print(weights)

    return None
