class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i, t in enumerate(temperatures):
            while st and t > st[-1][-1]:
                idx, temp = st.pop()
                ans[idx] = - idx + i
            st.append([i, t])
        return ans