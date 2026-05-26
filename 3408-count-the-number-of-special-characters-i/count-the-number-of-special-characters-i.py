class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        ans=set(word)
        for ch in ans:
            if ch.upper()  in ans and ch.islower():
                count+=1
        return count