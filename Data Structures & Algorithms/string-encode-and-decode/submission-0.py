class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            num = int(num)
            i += 1
            item = ""
            for j in range(num):
                item += s[i]
                i += 1
            res.append(item)
        return res