class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())
    

sol = Solution()
strs_input = ["act","pots","tops","cat","stop","hat"]
sol.groupAnagrams(strs_input)