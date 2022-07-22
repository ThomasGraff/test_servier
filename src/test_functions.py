import unittest
import pandas as pd

from cleaning import clean_data
from json_save import json_convertion
from transformation import all_mentions, mention_article


class TestFunctions(unittest.TestCase):
    def test_clean_data(self):
        self.assertRaises(TypeError, clean_data, "test")

    def test_transformation_mention_article(self):
        df = pd.DataFrame()
        self.assertRaises(TypeError, mention_article, "test", df)
        self.assertRaises(TypeError, mention_article, df, "test")
        self.assertRaises(TypeError, mention_article, "test", "test")

    def test_transformation_all_mentions(self):
        df = pd.DataFrame()
        self.assertRaises(TypeError, all_mentions, "test", df)
        self.assertRaises(TypeError, all_mentions, df, "test")
        self.assertRaises(TypeError, all_mentions, "test", "test")

    def test_json(self):
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        self.assertRaises(TypeError, json_convertion, "path", df2)
        self.assertRaises(TypeError, json_convertion, "path", "path")
        self.assertRaises(TypeError, json_convertion, df1, df2)


if __name__ == "__main__":
    unittest.main()
