import itertools


def fix_wiring(cables, sockets, plugs):
    return (
        f"plug {c} into {s} using {p}"
        if p else
        f"weld {c} to {s} without plug"
        for c, s, p in itertools.zip_longest(
            filter(lambda x: isinstance(x, str), cables),
            filter(lambda x: isinstance(x, str), sockets),
            filter(lambda x: isinstance(x, str), plugs),
        )
        if c is not None and s is not None
    )


plugs = ['plug1', 'plug2', 'plug3']
sockets = ['socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable1', 'cable2', 'cable3', 'cable4']

for c in fix_wiring(cables, sockets, plugs):
    print(c)
print("")
plugs = ['plugZ', None, 'plugY', 'plugX']
sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable2', 'cable1', False]

for c in fix_wiring(cables, sockets, plugs):
    print(c)
