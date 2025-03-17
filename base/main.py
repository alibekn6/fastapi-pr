from pydantic import BaseModel
from typing import Union, cast
from dataclasses import dataclass
from typing import List


class ItemList(BaseModel):
    items: List[str]


def process_items_pydantic(item_list: ItemList):
    for item in item_list.items:

        print(item)


itemlist1 = ItemList(items=["aas", "adweq"])
process_items_pydantic(itemlist1)


# other weak variant (typing)
def process_items_weak(item_list: List[str]):
    for item in item_list:
        if isinstance(item, str):
            print(item)
        raise ValueError("Passed not string")


itemlist1 = [12, "wed"]
process_items_weak(itemlist1)


# Appropriate annotation
def add(a, b):
    return a + b


add("as", "as")


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    email: str = "name@example.com"  # default

    def description(self) -> str:
        return f"{self.name} is this old: {self.age}"


def name_age(name: str, age: Union[int, str]) -> str:
    if isinstance(age, str):
        try:
            age = int(age)
        except ValueError:
            raise TypeError(
                "Age must be an integer or a string that can be converted to an integer"
            )

    person = Person(name=name, age=cast(int, age))
    return person.description()


# class Clock:
#     __DAY:int = 86400

#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Seconds must be in Integer type")
#         self.seconds = seconds % self.__DAY

#     def __eq__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError("type int or clock")

#         sc : int | Clock = other.seconds if isinstance(other, Clock) else other
#         return self.seconds == sc

# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 == c2)
# print(c1 == 1000)
