class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]

        curr_node.endOfWord = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return curr_node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]

        return True


trie = Trie()
print([trie.insert("apple"), trie.search("apple"), trie.search("app"),
      trie.startsWith("app"), trie.insert("app"), trie.search("app")])
