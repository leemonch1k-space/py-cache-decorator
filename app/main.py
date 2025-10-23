from typing import Callable


def cache(func: Callable) -> Callable:
    saved_cache = {}
    def wrapper(*args, **kwargs) -> int:
        nonlocal saved_cache

        if args in saved_cache:
            print("Getting from cache")
            return saved_cache[args]
        else:
            print("Calculating new result")
            saved_cache[args] = func(*args, **kwargs)
            return saved_cache[args]

    return wrapper
