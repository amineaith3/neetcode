class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toAnag(s:str)->str:
            return "".join(list(sorted([x for x in s])))
        hmap = defaultdict(list)
        for word in strs:
            hmap[toAnag(word)].append(word)
        ans = []
        for val in hmap.values():
            ans.append(val)
        return ans