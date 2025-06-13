from pathlib import Path

from cache.core import read_cache


def test_simple(fs):
    class Counter:
        c: int = 0

        @classmethod
        def create(cls):
            cls.c += 1
            return {}

    assert Counter.c == 0

    read_cache(Path('a'), Counter.create, False)
    read_cache(Path('b'), Counter.create, False)
    assert Counter.c == 2

    read_cache(Path('a'), Counter.create, False)
    read_cache(Path('c'), Counter.create, False)
    assert Counter.c == 3
