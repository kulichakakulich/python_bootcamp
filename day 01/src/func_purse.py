def squeak(func):
    def wrapper(purse):
        print("SQUEAK")
        return func(purse)
    return wrapper


@squeak
def add_ingot(purse: dict):
    new_purse = dict(purse)
    ingots = new_purse.get("gold_ingots", 0)
    new_purse["gold_ingots"] = ingots + 1
    return new_purse


@squeak
def get_ingot(purse: dict):
    new_purse = dict(purse)
    ingots = new_purse.get("gold_ingots", 0)
    if ingots > 0:
        new_purse["gold_ingots"] = ingots - 1
    return new_purse


@squeak
def empty(purse: dict):
    new_purse = dict(purse)
    for key in list(new_purse.keys()):
        new_purse.popitem()
    return new_purse
