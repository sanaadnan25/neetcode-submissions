class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair = {}

        for s in strs:
            sort = str(sorted(s))
            if sort not in pair:
                pair[sort] = [s]
            else:
                pair[sort].append(s)
        final = []
        for val in pair.values():
            final.append(val)
        return final

