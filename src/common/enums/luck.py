import enum


class LuckEnum(str, enum.Enum):
    GREAT = "大吉"
    NICE = "中吉"
    GOOD = "小吉"
    BAD = "中凶"
    TERROR = "大凶"
    UNKNOWN = ""
