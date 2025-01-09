from enum import Enum

class question_typeEnum(Enum):
    LONG_ANSWER = "LONG_ANSWER"
    SHORT_ANSWER = "SHORT_ANSWER"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    CHECK_BOX = "CHECK_BOX"


    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]