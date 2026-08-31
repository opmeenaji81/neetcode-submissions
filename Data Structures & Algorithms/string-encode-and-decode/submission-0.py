class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for char in strs:
            encoded_char = str(len(char))+ '#' + char
            encoded.append(encoded_char)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        store = []
        start = 0
        while start < len(s):
            length_end = s.find('#', start)
            length = int(s[start:length_end])
            starts = length_end + 1
            end = starts + length
            store.append(s[starts:end])
            start = end
        return store
