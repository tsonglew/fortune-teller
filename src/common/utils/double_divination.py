import json
from typing import Dict, List, Tuple, Union

from api.beans.divination import Divination
from api.beans.double_divination import DoubleDivination
from common.enums.element import ElementEnum
from common.utils.divination import DivinationUtil


class DoubleDivinationUtil:

    _value_to_double_divination_map: Dict[int, DoubleDivination]
    _name_to_double_divination_map: Dict[str, DoubleDivination]

    _divination_util: DivinationUtil

    _none = DoubleDivination(
        Divination("", 0, "", 0, ElementEnum.NONE),
        Divination("", 0, "", 0, ElementEnum.NONE),
        "",
        0,
        "",
        "",
    )

    def __init__(
        self,
        double_divination_json_path: str,
        double_divination_property_name_txt_path: str,
        divination_util: DivinationUtil,
    ):

        self._value_to_double_divination_map = {}
        self._name_to_double_divination_map = {}

        self._divination_util = divination_util

        property_name_mapping: Dict[str, str] = {}
        with open(double_divination_property_name_txt_path) as txt_file:
            for l in txt_file.readlines():
                s = l.split()
                property_name_mapping[s[1]] = s[0]

        with open(double_divination_json_path) as json_file:
            data = json.loads(json_file.read())

            entry: Dict[str, Union[str, int]]
            for entry in data["data"]:
                upper_divination_value, under_divination_value = divmod(
                    int(entry["value"]), 1 << 3
                )

                upper_divination = self._divination_util.get_divination_by_value(
                    upper_divination_value
                )
                under_divination = self._divination_util.get_divination_by_value(
                    under_divination_value
                )

                self._value_to_double_divination_map[
                    int(entry["value"])
                ] = DoubleDivination(
                    upper_divination,
                    under_divination,
                    str(entry["name"]),
                    int(entry["value"]),
                    str(entry["hexagram"]),
                    property_name_mapping.get(str(entry["name"])) or "",
                )
                self._name_to_double_divination_map[
                    str(entry["name"])
                ] = self._value_to_double_divination_map[int(entry["value"])]

    def get_double_divination_by_value(self, value: int) -> DoubleDivination:
        print(value)
        return self._value_to_double_divination_map.get(value) or self._none

    def get_double_divination_by_name(self, name: str) -> DoubleDivination:
        return self._name_to_double_divination_map.get(name) or self._none

    def get_double_divination_list(self) -> List[DoubleDivination]:
        return list(self._value_to_double_divination_map.values())

    def get_ti_yong_divination(
        self, double_divination: DoubleDivination, moving_line_idx: int
    ) -> Tuple[Divination, Divination]:

        ti_divination, yong_divination = (
            (
                double_divination.under,
                double_divination.upper,
            )
            if moving_line_idx < 3
            else (
                double_divination.upper,
                double_divination.under,
            )
        )
        return ti_divination, yong_divination

    def get_ben_double_divination(
        self, upper_divination: Divination, under_divination: Divination
    ) -> DoubleDivination:
        return self.get_double_divination_by_value(
            (upper_divination.value << 3) + under_divination.value
        )

    def get_bian_double_divination(
        self, ben_double_divination: DoubleDivination, moving_line_idx: int
    ) -> DoubleDivination:
        return self.get_double_divination_by_value(
            ben_double_divination.value ^ (1 << moving_line_idx)
        )
