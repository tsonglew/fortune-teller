from dataclasses import dataclass

from api.beans.divination import Divination
from api.beans.double_divination import DoubleDivination
from common.enums.luck import LuckEnum


class SubResult:
    divination_name: str
    double_divination: DoubleDivination
    ti_divination: Divination
    yong_divination: Divination
    luck: LuckEnum

    def __init__(
        self,
        divination_name: str,
        double_divination: DoubleDivination,
        ti_divination: Divination,
        yong_divination: Divination,
        luck: LuckEnum,
    ):
        self.divination_name = divination_name
        self.double_divination = double_divination
        self.ti_divination = ti_divination
        self.yong_divination = yong_divination
        self.luck = luck

    def to_json(self):
        return {
            self.divination_name: self.double_divination.to_json(),
            "体卦": self.ti_divination.to_json(),
            "用卦": self.yong_divination.to_json(),
            "状态": self.luck.value,
        }


@dataclass
class Result:
    start: SubResult
    process: SubResult
    end: SubResult
    moving_line_idx: int

    def to_json(self):
        return {
            "开始": self.start.to_json(),
            "过程": self.process.to_json(),
            "结果": self.end.to_json(),
            "动爻": self.moving_line_idx + 1,
        }
