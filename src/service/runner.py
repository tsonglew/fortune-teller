import datetime
from typing import List, Optional

from api.beans.chrono import Chrono
from api.beans.divination import Divination
from api.beans.double_divination import DoubleDivination
from api.beans.result import Result, SubResult
from common.utils.chrono import ChronoUtil
from common.utils.divination import DivinationUtil
from common.utils.double_divination import DoubleDivinationUtil
from common.utils.luck import LuckUtil
from common.utils.mutal_divination import MutualDivinationUtil


class RunnerService:

    _divination_util: DivinationUtil
    _double_divination_util: DoubleDivinationUtil
    _chrono_util: ChronoUtil
    _mutual_divination_util: MutualDivinationUtil
    _luck_util: LuckUtil

    def __init__(
        self,
        divination_util: DivinationUtil,
        double_divination_util: DoubleDivinationUtil,
        chrono_util: ChronoUtil,
        mutual_divination_util: MutualDivinationUtil,
        luck_util: LuckUtil,
    ):
        self._divination_util = divination_util
        self._double_divination_util = double_divination_util
        self._chrono_util = chrono_util
        self._mutual_divination_util = mutual_divination_util
        self._luck_util = luck_util

    def run(self, nums: List[int]) -> Optional[Result]:
        if len(nums) != 2:
            return None

        upper_divination = self._divination_util.get_divination_by_number(nums[0] % 8)
        under_divination = self._divination_util.get_divination_by_number(nums[1] % 8)

        ben_double_divination = self._double_divination_util.get_ben_double_divination(
            upper_divination, under_divination
        )
        moving_line_idx = self.get_moving_line_idx()

        bian_double_divination = (
            self._double_divination_util.get_bian_double_divination(
                ben_double_divination, moving_line_idx
            )
        )
        mutual_double_divination = self._mutual_divination_util.get_mutual_divination(
            ben_double_divination
        )

        return Result(
            start=SubResult(
                "主卦",
                ben_double_divination,
                *self._double_divination_util.get_ti_yong_divination(
                    ben_double_divination, moving_line_idx
                ),
                self._luck_util.get_luck(ben_double_divination, moving_line_idx)
            ),
            process=SubResult(
                "互卦",
                mutual_double_divination,
                *self._double_divination_util.get_ti_yong_divination(
                    mutual_double_divination, moving_line_idx
                ),
                self._luck_util.get_luck(mutual_double_divination, moving_line_idx)
            ),
            end=SubResult(
                "变卦",
                bian_double_divination,
                *self._double_divination_util.get_ti_yong_divination(
                    bian_double_divination, moving_line_idx
                ),
                self._luck_util.get_luck(bian_double_divination, moving_line_idx)
            ),
            moving_line_idx=moving_line_idx,
        )

    def get_moving_line_idx(self) -> int:
        return (
            self._chrono_util.get_chrono_by_datetime(datetime.datetime.now()).number - 1
        ) % 6
