class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for item in strs:
            res += str(len(item)) + "#" + item
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            i += 1
            num = int(num)
            j = i + num
            res.append(s[i:j])
            i = j
        
        return res