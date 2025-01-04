from trie import Trie
from typing import List


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings: List[str]) -> str:
        if not strings:  # Перевірка на порожній список
            return ""

        # Додавання всіх слів до Trie
        for word in strings:
            self.insert(word)

        # Пошук найдовшого спільного префікса
        prefix = ""
        node = self.root
        while node:
            if len(node.children) == 1 and not node.is_end_of_word:
                char = next(iter(node.children))  # Отримати єдину букву
                prefix += char
                node = node.children[char]
            else:
                break

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl", "Test 1 failed"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters", "Test 2 failed"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == "", "Test 3 failed"

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == "", "Test 4 failed"

    print("All tests passed!")
