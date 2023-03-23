import unittest
from func_purse import *
from splitwise import *


class TestCases(unittest.TestCase):
    def test_add_ingot(self):
        purse = {}
        new_purse = add_ingot(purse)
        assert new_purse == {"gold_ingots": 1}

        purse = {"gold_ingots": 3, "silver_ingots": 2}
        new_purse = add_ingot(purse)
        assert new_purse == {"gold_ingots": 4, "silver_ingots": 2}

    def test_get_ingot(self):
        purse = {}
        new_purse = get_ingot(purse)
        assert new_purse == {}

        purse = {"gold_ingots": 1}
        new_purse = get_ingot(purse)
        assert new_purse == {"gold_ingots": 0}

        purse = {"gold_ingots": 3, "silver_ingots": 2}
        new_purse = get_ingot(purse)
        assert new_purse == {"gold_ingots": 2, "silver_ingots": 2}

    def test_empty(self):
        purse = {}
        new_purse = empty(purse)
        assert new_purse == {}

        purse = {"gold_ingots": 3, "silver_ingots": 2}
        new_purse = empty(purse)
        assert new_purse == {}

    def test_split_booty(self):
        purse1 = {}
        new_purses = split_booty(purse1)
        assert new_purses == ({}, {}, {})

        purse1 = {"gold_ingots": 1}
        new_purses = split_booty(purse1)
        assert new_purses == ({"gold_ingots": 1}, {}, {})

        purse1 = {"gold_ingots": 2}
        new_purses = split_booty(purse1)
        assert new_purses == ({"gold_ingots": 1}, {"gold_ingots": 1}, {})

        purse1 = {"gold_ingots": 3}
        new_purses = split_booty(purse1)
        assert new_purses == ({"gold_ingots": 1}, {
            "gold_ingots": 1}, {"gold_ingots": 1})

        purse1 = {"gold_ingots": 4}
        purse2 = {"gold_ingots": 2, "silver_ingots": 1}
        purse3 = {}
        new_purses = split_booty(purse1, purse2, purse3)
        assert new_purses == (
            {"gold_ingots": 2},
            {"gold_ingots": 2},
            {"gold_ingots": 2}
        )

        purse1 = {"gold_ingots": 14}
        purse2 = {"gold_ingots": 28, "silver_ingots": 1}
        purse3 = {"gold_ingots": 1, "silver_ingots": 12}
        new_purses = split_booty(purse1, purse2, purse3)
        assert new_purses == (
            {"gold_ingots": 15},
            {"gold_ingots": 14},
            {"gold_ingots": 14}
        )


if __name__ == '__main__':
    unittest.main()
