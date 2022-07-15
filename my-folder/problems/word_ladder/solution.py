class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wList = set(wordList)
        queue = [(beginWord, 1)]
        visited = set(beginWord)
        while queue:
            (word, length) = queue.pop(0)
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i+1:]
                    if next_word in wList:
                        wList.remove(next_word)
                        if next_word == endWord:
                            return length + 1
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word, length + 1))
        return 0
                        