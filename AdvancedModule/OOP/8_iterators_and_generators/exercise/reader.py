def read_next(*args):
    for seq in args:
        yield from seq


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')


def read_nextt(*args):
    for seq in args:
        for el in seq:
            yield el


for item in read_nextt("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')


