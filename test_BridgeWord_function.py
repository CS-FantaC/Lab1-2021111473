import unittest
from unittest import TestCase
from main import searchBridgeWords
import torch

class BWTestCase(TestCase):
    def test1(self):
        BW = searchBridgeWords("How", "showers")
        self.assertEqual(BW, ["many"])

    def test2(self):
        BW = searchBridgeWords("How", "are")
        self.assertEqual(BW, ["old", "wasted"])


    def test3(self):
        BW = searchBridgeWords("my", "sister")
        self.assertEqual(BW, [])

    def test4(self):
        BW = searchBridgeWords(0.1, torch.Tensor([1, 2, 3]))
        self.assertEqual(BW, [])

    def test5(self):
        BW = searchBridgeWords("Julius", "Oppenheimer")
        self.assertEqual(BW, [])


if __name__ == "__main__":
    unittest.main()