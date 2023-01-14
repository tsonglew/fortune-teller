import enum


class ElementEnum(str, enum.Enum):
    FIRE = "火"
    WATER = "水"
    WOOD = "木"
    EARTH = "土"
    GOLD = "金"
    NONE = ""
