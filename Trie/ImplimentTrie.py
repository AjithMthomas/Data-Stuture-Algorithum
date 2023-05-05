class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word
# create a new Trie instance
trie = Trie()

# insert some strings into the trie
trie.insert('hello')
trie.insert('world')
trie.insert('hey')
trie.insert('hi')

# search for some strings in the trie
print(trie.search('hello'))  # output: True
print(trie.search('world'))  # output: True
print(trie.search('hey'))    # output: True
print(trie.search('hi'))     # output: True
print(trie.search('foo'))    # output: False
