class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            letter_count = [0] * 26
            for i in s:
                letter_count[ord(i) - ord('a')] += 1
            letter_count = tuple(letter_count)
            if letter_count not in d:
                d[letter_count] = []
            d[letter_count].append(s)
        
        res = []
        for key, item in d.items():
            list(item)
            res.append(item)

        return res