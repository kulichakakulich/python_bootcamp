from func_purse import *


def split_booty(*purses: dict):
    ingots = [purse.get("gold_ingots", 0) for purse in purses]
    total_ingots = sum(ingots)
    min_ingots = total_ingots // 3
    remainder = total_ingots % 3
    new_purses = []
    for i in range(3):
        target = min_ingots + int(i < remainder)
        new_purse = empty({})
        while target > 0:
            new_purse = add_ingot(new_purse)
            target -= 1

        new_purses.append(new_purse)
    return tuple(new_purses)
