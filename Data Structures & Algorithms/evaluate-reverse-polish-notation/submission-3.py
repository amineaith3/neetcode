class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = int(st.pop())
                a = int(st.pop())
                if token == '+':
                    st.append(a + b)
                elif token == '*':
                    st.append(a * b)
                elif token == '-':
                    st.append(a - b)
                else:
                    st.append(int(a /b))
            else:
                st.append(int(token))
        return st[0]
