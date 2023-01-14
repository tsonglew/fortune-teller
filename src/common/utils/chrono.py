import datetime
import json
from typing import Dict, List, Union

from api.beans.chrono import Chrono


class ChronoUtil:

    _value_to_chrono_map: Dict[int, Chrono]

    _none = Chrono("", 0)

    def __init__(self, chrono_json_path: str):
        self._value_to_chrono_map = {}

        with open(chrono_json_path) as json_file:
            data = json.loads(json_file.read())

            entry: Dict[str, Union[str, int]]
            for entry in data["data"]:
                self._value_to_chrono_map[int(entry["number"])] = Chrono(
                    str(entry["name"]),
                    int(entry["number"]),
                )

    def get_chrono_by_number(self, number: int) -> Chrono:
        return self._value_to_chrono_map.get(number) or self._none

    def get_chrono_list(self) -> List[Chrono]:
        return list(self._value_to_chrono_map.values())

    def get_chrono_by_datetime(self, dt: datetime.datetime) -> Chrono:
        return self.get_chrono_by_number((dt.hour + 1) // 2 % 12 + 1)
