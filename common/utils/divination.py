import json
from typing import Dict, List, Optional, Union

from api.beans.divination import Divination
from common.enums.element import ElementEnum


class DivinationUtil:

    _value_to_divination_map: Dict[int, Divination]
    _name_to_divination_map: Dict[str, Divination]
    _number_to_divination_map: Dict[int, Divination]

    _none = Divination("", 0, "", 0, ElementEnum.NONE)

    def __init__(self, divination_json_path: str):
        self._value_to_divination_map = {}
        self._name_to_divination_map = {}
        self._number_to_divination_map = {}

        with open(divination_json_path) as json_file:
            data = json.loads(json_file.read())

            entry: Dict[str, Union[str, int]]
            for entry in data["data"]:
                d = Divination(
                    str(entry["name"]),
                    int(entry["value"]),
                    str(entry["hexagram"]),
                    int(entry["number"]),
                    ElementEnum(entry["element"]),
                )
                self._number_to_divination_map[d.number] = self._name_to_divination_map[
                    d.name
                ] = self._value_to_divination_map[d.value] = d

    def get_divination_by_value(self, value: int) -> Divination:
        return self._value_to_divination_map.get(value) or self._none

    def get_divination_by_name(self, name: str) -> Divination:
        return self._name_to_divination_map.get(name) or self._none

    def get_divination_by_number(self, number: int) -> Divination:
        return self._number_to_divination_map.get(number) or self._none

    def get_divination_list(self) -> List[Divination]:
        return list(self._value_to_divination_map.values())
