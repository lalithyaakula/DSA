class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        root = TrieNode()

        # -----------------------------------
        # function to update best index
        # -----------------------------------
        def update(node, idx):
            
            # first insertion
            if node.index == -1:
                node.index = idx
                return
            
            old_idx = node.index
            
            old_word = wordsContainer[old_idx]
            new_word = wordsContainer[idx]
            
            # choose smaller length
            if len(new_word) < len(old_word):
                node.index = idx
        
        # -----------------------------------
        # Build Trie
        # -----------------------------------
        for i, word in enumerate(wordsContainer):
            
            node = root
            
            # update root node also
            update(node, i)
            
            # reverse word for suffix matching
            for ch in reversed(word):
                
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                node = node.children[ch]
                
                update(node, i)
        
        # -----------------------------------
        # Process Queries
        # -----------------------------------
        ans = []
        
        for word in wordsQuery:
            
            node = root
            
            for ch in reversed(word):
                
                if ch not in node.children:
                    break
                
                node = node.children[ch]
            
            ans.append(node.index)
        
        return ans