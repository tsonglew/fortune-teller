from dataclasses import dataclass

from api.beans.divination import Divination
from api.beans.double_divination import DoubleDivination


class SubResult:
    divination_name: str
    double_divination: DoubleDivination
    ti_divination: Divination
    yong_divination: Divination

    def __init__(
        self,
        divination_name: str,
        double_divination: DoubleDivination,
        ti_divination: Divination,
        yong_divination: Divination,
    ):
        self.divination_name = divination_name
        self.double_divination = double_divination
        self.ti_divination = ti_divination
        self.yong_divination = yong_divination

    def to_json(self):
        return {
            self.divination_name: self.double_divination.to_json(),
            "体卦": self.ti_divination.to_json(),
            "用卦": self.yong_divination.to_json(),
        }


@dataclass
class Result:
    start: SubResult
    process: SubResult
    end: SubResult

    def to_json(self):
        return {
            "开始": self.start.to_json(),
            "过程": self.process.to_json(),
            "结果": self.end.to_json(),
        }
