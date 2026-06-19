import unittest
from huffman import get_char_frequency

class TestHuffman(unittest.TestCase):
    def test_frequency(self):
        # 测试 hello 单词的字母频率是否计算正确
        result = get_char_frequency("hello")
        self.assertEqual(result['l'], 2)
        self.assertEqual(result['h'], 1)

if __name__ == '__main__':
    unittest.main()
