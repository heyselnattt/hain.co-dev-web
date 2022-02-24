from enum import IntEnum


class TransactionType(IntEnum):
    """Enum to describe a transaction type

    ORDER - A transaction from the mobile application
    BUY - A transaction from the walk in customers
    ADMIN - Transactions done by admins
    """
    ORDER = 0
    BUY = 1
    ADMIN = 2
