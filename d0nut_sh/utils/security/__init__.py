from enum import Enum

class Authorization(Enum):
    Guest = 1 << 0
    User = 1 << 1
    Admin = 1 << 2
