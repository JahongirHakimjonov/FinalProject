class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        return len(s.split()[-1])


# LeetCode ni o'zida run qilib ko'ring.
