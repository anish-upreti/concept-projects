from trie import Trie

# ── Setup ──────────────────────────────────────────────
trie = Trie()
words = ["cat", "car", "card", "care", "careful", "dog", "door", "done", "donate", "python", "prefix", "pre"]
for word in words:
    trie.insert(word)

# ── search() ───────────────────────────────────────────
print("=== search() ===")
print(trie.search("car"))       # True
print(trie.search("care"))      # True
print(trie.search("ca"))        # False - prefix only, not a word
print(trie.search("xyz"))       # False - doesn't exist
print(trie.search("pre"))       # True - inserted as a word

# ── starts_with() ──────────────────────────────────────
print("\n=== starts_with() ===")
print(trie.starts_with("ca"))   # True
print(trie.starts_with("do"))   # True
print(trie.starts_with("pre"))  # True
print(trie.starts_with("xyz"))  # False

# ── autocomplete() ─────────────────────────────────────
print("\n=== autocomplete() ===")
print(trie.autocomplete("ca"))      # ['cat', 'car', 'card', 'care', 'careful']
print(trie.autocomplete("do"))      # ['dog', 'door', 'done', 'donate']
print(trie.autocomplete("pre"))     # ['pre', 'prefix']
print(trie.autocomplete("xyz"))     # []

# ── frequency ranking ──────────────────────────────────
print("\n=== frequency ranking ===")
trie.search("careful")
trie.search("careful")
trie.search("careful")
trie.search("care")
trie.search("care")
trie.search("car")


# care(3) = careful(3) > car(2) > cat(0) = card(0)

print(trie.autocomplete("ca"))

# ── large vocabulary ───────────────────────────────────
print("\n=== large vocabulary ===")
with open("/usr/share/dict/words") as f:
    dict_words = [line.strip().lower() for line in f]

big_trie = Trie()
for word in dict_words:
    big_trie.insert(word)

print(f"Total words loaded: {len(dict_words)}")
print(f"autocomplete('pre'): {len(big_trie.autocomplete('pre'))} results →", big_trie.autocomplete("pre")[:5], "...")
print(f"autocomplete('com'): {len(big_trie.autocomplete('com'))} results →", big_trie.autocomplete("com")[:5], "...")
print(f"autocomplete('xyz'): {big_trie.autocomplete('xyz')}")
