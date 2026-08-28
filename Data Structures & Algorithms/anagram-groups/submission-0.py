class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            

            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]]

        return list(groups.values())
            