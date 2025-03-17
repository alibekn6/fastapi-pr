# Checking types

from typing import List, Union


# other weak variant (typing)
def process_items(item_list: List[str]):
    for item in item_list:
        print(item)


itemlist1 = ["As", "wed"]
itemlist2 = [12, True]
process_items(itemlist1)


def process_items_safe(item: Union[str, int]) -> None:
    if isinstance(item, str):
        print(f"String : {item}")
    elif isinstance(item, int):
        print(f"Integer : {item}")
    else:
        raise TypeError("Unsupported type")


process_items_safe(23)
process_items_safe("asd")


# !!!Check with mypy!!!
