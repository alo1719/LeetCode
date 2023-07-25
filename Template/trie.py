class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False
        
    def insert(self, word):
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.is_end = True
        
    # optional
    def remove(self, word):
        def _remove(node, word, depth):
            if depth == len(word):
                node.is_end = False
                return len(node.children) == 0  # this node has no children
            ch = word[depth]
            if ch not in node.children: return False  # word not in trie
            if _remove(node.children[ch], word, depth+1):
                del node.children[ch]
                return len(node.children) == 0
            return False  #  this node has children, cannot be removed
        _remove(self, word, 0)
    
    # need customizaiton
    def search(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children: return False  # no such word, can return something else
            cur = cur.children[ch]
            # can do something here
        return cur.is_end  # match the whole word
        return True  # match prefix