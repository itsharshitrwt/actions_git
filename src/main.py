# Sample addition
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def test():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1

    