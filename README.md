## Задача 1. Розширення функціоналу префіксного дерева

Реалізуйте два додаткових методи для класу `Trie`:

- `count_words_with_suffix(pattern)` для підрахунку кількості слів, що закінчуються заданим шаблоном;
- `has_prefix(prefix)` для перевірки наявності слів із заданим префіксом.

**Технічні умови**

1. Клас `Homework` має успадковувати базовий клас `Trie`.
2. Методи повинні опрацьовувати помилки введення некоректних даних.
3. Вхідні параметри обох методів мають бути рядками.
4. Метод `count_words_with_suffix` має повертати ціле число.
5. Метод `has_prefix` має повертати булеве значення.

Шаблон програми

```
from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        pass

    def has_prefix(self, prefix) -> bool:
       pass

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

```

## Задача 2. Пошук найдовшого спільного префікса

Створіть клас `LongestCommonWord`, який наслідує клас `Trie`, та реалізуйте метод `find_longest_common_word`, який знаходить найдовший спільний префікс для всіх слів у вхідному масиві рядків `strings`.

**Технічні умови**

1. Клас `LongestCommonWord` має успадковувати `Trie`.
2. Вхідний параметр методу `find_longest_common_word`, `strings` — масив рядків.
3. Метод `find_longest_common_word` має повертати рядок — найдовший спільний префікс.
4. Час виконання — O(S), де
   S — сумарна довжина всіх рядків.

Шаблон програми

```
from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        pass

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
```
