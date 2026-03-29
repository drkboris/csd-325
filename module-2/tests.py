from week9_assignment import Trie
def test_trie():
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")

    return [
        (trie.search("hello"), True, "Search for 'hello'"),  # Test 1
        (trie.search("world"), True, "Search for 'world'"),  # Test 2
        (trie.startsWith("he"), True, "Prefix search for 'he'"),  # Test 3
        (trie.search("unknown"), False, "Search for 'unknown'")  # Test 4
    ]
