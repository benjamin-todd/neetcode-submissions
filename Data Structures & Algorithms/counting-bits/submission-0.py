class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        res = []

        while i <= n:
            c = 0
            for j in bin(i):
                if j == "1":
                    c +=1
            i += 1
            res.append(c)
        
        return res