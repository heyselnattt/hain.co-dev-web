from enum import IntEnum


class ProductType(IntEnum):
    """Enum to describe the type of product, to be used with dropdowns in
    the client application
    """
    BREAKFAST = 0
    LUNCH = 1
    DESSERT = 2
    EXTRA = 3