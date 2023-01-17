from typing import Dict, List, Union

from common.utils.double_divination import DoubleDivinationUtil


class DoubleDivinationService:

    _double_divination_util: DoubleDivinationUtil

    def __init__(self, double_divination_util: DoubleDivinationUtil):
        self._double_divination_util = double_divination_util

    @property
    def double_divination_util(self):
        return self._double_divination_util

    def get_divination_list(
        self,
    ) -> List[Dict[str, Union[str, int, Dict[str, Union[str, int]]]]]:
        return [
            double_divination.to_json()
            for double_divination in self.double_divination_util.get_double_divination_list()
        ]
