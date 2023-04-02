from typing import Dict, Union

from api.beans.divination import Divination


class DoubleDivination:
    _upper: Divination
    _under: Divination

    _name: str
    _value: int
    _hexagram: str
    _property_name: str
    _desc: str

    def __init__(
            self,
            upper: Divination,
            under: Divination,
            name: str,
            value: int,
            hexagram: str,
            property_name: str,
            desc: str,
            detail: str
    ) -> None:
        self._upper = upper
        self._under = under

        self._name = name
        self._value = value
        self._hexagram = hexagram
        self._property_name = property_name or ""
        self._desc = desc
        self._detail = detail

    @property
    def upper(self) -> Divination:
        return self._upper

    @property
    def under(self) -> Divination:
        return self._under

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
    def property_name(self) -> str:
        return self._property_name

    @property
    def desc(self) -> str:
        return self._desc

    @property
    def detail(self) -> str:
        return self._detail

    def to_json(self) -> Dict[str, Union[str, int, Dict[str, Union[str, int]]]]:
        return {
            "upper": self.upper.to_json(),
            "under": self.under.to_json(),
            "name": self.name,
            "value": self.value,
            "hexagram": self.hexagram,
            "property_name": self.property_name,
            "desc": self.desc,
            "detail": self.detail
        }
