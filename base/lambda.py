from typing import List


def map(func, data):
    result: list = []
    for item in data:
        new_item = func(item)
        result.append(new_item)
    return result

numbers: List[int] = [13,4,5,5,34,3,23]
print(numbers)
