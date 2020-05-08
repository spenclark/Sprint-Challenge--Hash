def intersection(arrays):

    """
    YOUR CODE HERE
    """ 
   
    items = dict()
    result = []

    for i, num_list in enumerate(arrays):
        for y in num_list:
            if items.get(y) != None and i > 0:
                items[y] = items[y] + 1
            elif items.get(y) is None and i == 0: 
                items[y] = 1
            else:
                continue

    for num in items:
        if items[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
