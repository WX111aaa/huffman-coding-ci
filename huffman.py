def get_char_frequency(text):
    """计算输入文本的字符频率"""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq
