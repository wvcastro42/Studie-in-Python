"""In a given list the first element should become the last one. An empty list or list with only one element should stay the same."""
from typing import Iterable
def replace_first(items: list) -> Iterable:
    if len(items) > 0:
        items.append(items[0])
        items.pop(0)
    return items

print(replace_first([1, 2, 3, 4]))
