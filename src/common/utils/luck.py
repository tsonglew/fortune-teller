from typing import Optional

from api.beans.double_divination import DoubleDivination
from common.enums.element import ElementEnum
from common.enums.luck import LuckEnum
from common.utils.double_divination import DoubleDivinationUtil


class LuckUtil:

    _double_divination_util: DoubleDivinationUtil

    _generation_map = {
        ElementEnum.FIRE: ElementEnum.EARTH,
        ElementEnum.EARTH: ElementEnum.GOLD,
        ElementEnum.GOLD: ElementEnum.WATER,
        ElementEnum.WATER: ElementEnum.WOOD,
        ElementEnum.WOOD: ElementEnum.FIRE,
    }
    _restriction_map = {
        ElementEnum.FIRE: ElementEnum.GOLD,
        ElementEnum.EARTH: ElementEnum.WATER,
        ElementEnum.GOLD: ElementEnum.WOOD,
        ElementEnum.WATER: ElementEnum.FIRE,
        ElementEnum.WOOD: ElementEnum.EARTH,
    }

    def __init__(self, double_divination_util: DoubleDivinationUtil):
        self._double_divination_util = double_divination_util

    def get_luck(
        self, double_divination: DoubleDivination, moving_line_idx: int
    ) -> Optional[LuckEnum]:
        (
            ti_divination,
            yong_divination,
        ) = self._double_divination_util.get_ti_yong_divination(
            double_divination, moving_line_idx
        )
        if self._generation_map.get(yong_divination.element) == ti_divination.element:
            return LuckEnum.GREAT
        if yong_divination.element == ti_divination.element:
            return LuckEnum.NICE
        if self._restriction_map.get(ti_divination.element) == yong_divination.element:
            return LuckEnum.GOOD
        if self._generation_map.get(ti_divination.element) == yong_divination.element:
            return LuckEnum.BAD
        if self._restriction_map.get(yong_divination.element) == ti_divination.element:
            return LuckEnum.TERROR
