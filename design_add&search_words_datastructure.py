class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, 0, self.trie)

    def _search_in_node(self, word, index, node):
        if index == len(word):
            return '#' in node
        
        char = word[index]
        if char == '.':
            for child in node.values():
                if isinstance(child, dict) and self._search_in_node(word, index + 1, child):
                    return True
            return False
        elif char in node:
            return self._search_in_node(word, index + 1, node[char])
        else:
            return False

# Sample test cases
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True
