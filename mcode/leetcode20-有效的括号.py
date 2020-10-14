class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','[':']','{':'}'}
        cache = []
        for c in s:
            # 如果是左括号 入栈
            if c in mapping:
                cache.append(c)
            # 如果 栈中已经有左括号，此时要匹配是否与栈中的左括号匹配
            elif len(cache)>0 and mapping[cache[-1]] == c:
                # 如果匹配则出栈
                cache.pop()
            # 如果栈中无左括号，此时字符串中只有右括号
            else:
                return False
        return len(cache) == 0

if __name__ == '__main__':
    st = '[][]'
    s = Solution()
    print(s.isValid(st))