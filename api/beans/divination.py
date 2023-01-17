from typing import Dict, Union

from common.enums.element import ElementEnum


class Divination:

    _name: str
    _value: int
    _hexagram: str
    _number: int
    _element: ElementEnum

    def __init__(
        self, name: str, value: int, hexagram: str, number: int, element: ElementEnum
    ):
        self._name = name
        self._value = value
        self._hexagram = hexagram
        self._number = number
        self._element = element

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> int:
        return self._value

    @property
    def hexagram(self) -> str:
        return self._hexagram

    @property
    def number(self) -> int:
        return self._number

    @property
    def element(self) -> ElementEnum:
        return self._element

    def to_json(self) -> Dict[str, Union[str, int]]:
        return {
            "name": self.name,
            "value": self.value,
            "hexagram": self.hexagram,
            "number": self.number,
            "element": self.element.value,
        }
