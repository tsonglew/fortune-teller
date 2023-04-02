from unittest import TestCase

from common.utils.description import DescriptionUtil


class TestDescriptionUtil(TestCase):
    description_util = DescriptionUtil("../../assets/doubleDivinationDesc.xlsx")

    def test_len(self):
        self.assertEqual(len(self.description_util.description_map), 64)
