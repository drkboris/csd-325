# ===========================================
# Title: assign_2.2py
# Author: Zach Donohue
# Date: 26 March 2026
# Modified By: Zach Donohue
# Description: Taken from my week 9 assignment from CS420-T301 Data Structures Class.
# ============================================

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            # If the character doesn't exist as a child node, create one
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        # Mark the final node as the end of a complete word
        current.is_end_of_word = True

    def startsWith(self, prefix):
        """
        Returns True if any word in the trie starts with the given prefix.
        Returns False if no word starts with that prefix.
        """
        current = self.root

        for char in prefix:
            # If the character doesn't exist in the trie return fals
            if char not in current.children:
                return False
            # Move down to the next node and continue checking
            current = current.children[char]

        return True


# Populate the trie with some words
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("help")
trie.insert("helicopter")

# Test inputs that will hit both return paths
print(trie.startsWith("he"))          # True  - matches hello, help, helicopter
print(trie.startsWith("hel"))         # True  - matches hello, help, helicopter
print(trie.startsWith("wor"))         # True  - matches world
print(trie.startsWith("xyz"))         # False - no match, hits the return False path
print(trie.startsWith("hellop"))      # False - goes deep but falls off the end
print(trie.startsWith(""))            # True  - empty prefix always matches