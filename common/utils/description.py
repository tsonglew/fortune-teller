from typing import Dict

import pandas


class DescriptionUtil:
    def __init__(self, description_xls_path: str):
        self._description_map = {}
        df = pandas.read_excel(
            description_xls_path,
            engine='openpyxl',
            index_col=0,
        )

        for index, row in df.iterrows():
            self._description_map[index] = {
                'desc': row[0],
                'detail': row[1],
            }

    @property
    def description_map(self):
        return self._description_map

    def get_description(self, key: str) -> Dict[str, str]:
        return self._description_map.get(key) or {'desc': '', 'detail': ''}
