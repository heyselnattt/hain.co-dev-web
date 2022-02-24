from enum import IntEnum


class TransactionType(IntEnum):
    """Enum to describe a transaction type

    ``Attributes:``
        ORDER (int): A transaction from the mobile application
        BUY (int): A transaction from the walk in customers
        ADMIN (int): Transactions done by admins
    """
    ORDER = 0
    BUY = 1
    ADMIN = 2
