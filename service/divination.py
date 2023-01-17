from typing import Dict, List, Union

from common.utils.divination import DivinationUtil


class DivinationService:

    _divination_util: DivinationUtil

    def __init__(self, divination_util: DivinationUtil):
        self._divination_util = divination_util

    @property
    def divination_util(self):
        return self._divination_util

    def get_divination_list(self) -> List[Dict[str, Union[str, int]]]:
        return [
            divination.to_json()
            for divination in self.divination_util.get_divination_list()
        ]
