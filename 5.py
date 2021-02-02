class Solution:
    def interpret(self, command: str) -> str:
        a = []
        n = len(command)
        l = 0
        i = 0
        ans = ""
        s = command+"qwertyqwre"
        while i<n:
            if s[i] == 'G':
                # a.append('G')
                ans+="G"
                i+=1
            if s[i] == '(' and s[i+1] == 'a':
                # a.append("al")
                ans+="al"
                i+=4
            if s[i] == '(' and s[i+1] == ')':
                # a.append("o")
                ans+="o"
                i+=2
        # for i in a:
        #     print(i, end='')
        # print(s)
        return ans
        