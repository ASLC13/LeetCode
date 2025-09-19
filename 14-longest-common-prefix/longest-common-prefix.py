class Solution:
    def substr(self, str1, str2) -> str:
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] == str2[i]:
                continue
            return str1[0:i]
        return str1[0: min_len]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for i in range(1,len(strs)):
            s = self.substr(s, strs[i])
        return s

        