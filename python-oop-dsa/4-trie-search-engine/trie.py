class TrieNode:
    def __init__(self):
        self.frequency = 0 # we increment frequency only on nodes where is_end_of_word is true, intermediate nodes have it but it's never used
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]  # it runs every iteration whether the node was just created or already existed, it is to move the current pointer forward
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        current.frequency += 1   # we increase the frequency only on search not insert, it will reflect how often a word is looked up
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    def autocomplete(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        results = []
        self._dfs(current, prefix, results)
        results = sorted(results, key = lambda x: x[0], reverse=True) 
        results = [word for freq, word in results]  # since the result is tuple we extract only the words after sorting
        return results
    
    def _dfs(self, node, current_word, results):
        if node.is_end_of_word:
            results.append((node.frequency, current_word))  # returns a tuple with frequency and the current word
        for char, child in node.children.items():
            self._dfs(child, current_word + char, results)
            