def lstSquare(n: int) -> list:
    return list(map(lambda i: i * i, range(1, n + 1)))


print(lstSquare(3))


def lessThan(lst: list, n: int) -> list:
    return [i for i in lst if i < n]

print(lessThan([1, 2, 3, 4, 5], 4))


def flatten1(lst: list) -> list:
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])


def flatten2(lst: list) -> list:
    return [element for sublist in lst for element in sublist]


print(flatten2([[1, 2, 3], [4, 5], [6, 7]]))


# Let lst be a list of a list of element, use high-order function approach to write function flatten(lst) that returns the list of all elements


def flatten3(lst: list) -> list:
    return reduce(lambda x, y: x + y, lst)

print(flatten3([[1, 2, 3], [4, 5], [6, 7]]))