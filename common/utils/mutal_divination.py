import json
from typing import Dict

from api.beans.double_divination import DoubleDivination
from common.utils.double_divination import DoubleDivinationUtil


class MutualDivinationUtil:

    _divination_mapping: Dict[DoubleDivination, DoubleDivination]

    _double_divination_util: DoubleDivinationUtil

    def __init__(
        self,
        mutual_divination_txt_path: str,
        double_divination_util: DoubleDivinationUtil,
    ):
        self._divination_mapping = {}

        self._double_divination_util = double_divination_util
        with open(mutual_divination_txt_path) as f:
            for l in f.readlines():
                s = l.split()

                divination = self._double_divination_util.get_double_divination_by_name(
                    s[0]
                )
                self._divination_mapping[
                    divination
                ] = self._double_divination_util.get_double_divination_by_name(s[2])

    def get_mutual_divination(self, double_divination: DoubleDivination):
        return (
            self._divination_mapping.get(double_divination)
            or DoubleDivinationUtil._none
        )
