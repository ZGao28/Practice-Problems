class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            if i == 0:
                ans += arr[i] * arr[i+1]
            elif i == len(arr) - 1:
                ans += arr[i] * arr[i-1]
            else:
                ans += arr[i] * min(arr[i-1], arr[i+1])
            arr.pop(i)
        return ans
