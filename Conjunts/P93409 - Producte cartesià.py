

def cartesian_product(a: set[int], b: set[int]) -> set[tuple[int, int]]:
    return {(x, y) for y in b for x in a}