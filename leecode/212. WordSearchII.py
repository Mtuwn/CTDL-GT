from typing import List

class Trie:
    def __init__(self):
        self.children: List[Trie | None] = [None] * 26
        
        self.ref: int = -1
    
    def insert(self, word: str, ref: int):
        node = self

        for char in word:
            index = ord(char) - ord('a')

            if node.children[index] is None:
                node.children[index] =  Trie()
            node = node.children[index]
        
        node.ref = ref


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node: Trie, i:int, j: int):
            index = ord(board[i][j]) - ord('a')

            if node.children[index] is None:
                return
            
            node = node.children[index]

            if node.ref >= 0:
                ans.append(words[node.ref])
                node.ref = -1
            
            temp_char = board[i][j]
            board[i][j] = '#'

            directions = [(-1,0), (0,1), (1,0), (0,-1)]

            for dx, dy in directions:
                new_dx, new_dy = i + dx, j + dy

                if 0 <= new_dx < n  and 0 <= new_dy < m and board[new_dx][new_dy] != "#": 
                    dfs(node, new_dx, new_dy)
            
            board[i][j] = temp_char

        

        trie_root = Trie()
        for index, word in enumerate(words):
            trie_root.insert(word, index)
        
        n, m = len(board), len(board[0])

        ans = []

        for i in range(n):
            for j in range(m):
                dfs(trie_root, i, j)
        
        return ans



        

