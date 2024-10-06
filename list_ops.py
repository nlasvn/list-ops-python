def append(list1, list2):
    return list1 + list2


def concat(lists):
    return foldl(append, lists, [])


def filter(function, list):
    filtered_list = []

    for item in list:
        if function(item):
            filtered_list = append(filtered_list, [item])

    return filtered_list


def length(list):
    num = 0

    for _ in list:
        num += 1

    return num


def map(function, list):
    mapped = []

    for item in list:
        mapped = append(mapped, [function(item)])

    return mapped


def foldl(function, list, initial):
    acc = initial

    for item in list:
        acc = function(acc, item)

    return acc


def foldr(function, list, initial):
    acc = initial

    for item in list[::-1]:
        acc = function(acc, item)

    return acc


def reverse(list):
    return list[::-1]
