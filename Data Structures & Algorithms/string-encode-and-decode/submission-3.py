class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for s in strs:
            answer += s
            answer += "`"
        return answer

    def decode(self, s: str) -> List[str]:
        answer = []
        while "`" in s:
            first, second = s.split("`", 1)
            answer.append(first)
            s = second
        return answer
