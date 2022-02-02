def find(search_list, value):
    lower, upper = 0, len(search_list) - 1

    while lower <= upper:
        middle = (upper + lower) // 2
        if search_list[middle] == value:
            return middle

        if search_list[middle] > value:
            upper = middle - 1

        elif search_list[middle] < value:
            lower = middle + 1

    raise ValueError("value not in array")
