class Solution(object):
    def subsets_with_dup(self, nums):
        """
        Учитывая целочисленный массив nums, 
        который может содержать дубликаты, 
        вернуть все возможные подмножества.
        Набор решений не должен содержать повторяющихся
        подмножеств. Верните решение в любом порядке.

        Example 1:
        Input: nums = [1,2,2]
        Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

        Example 2:
        Input: nums = [0]
        Output: [[],[0]]

        """

        n = len(nums)
        answer = []
        for i in range(2 ** n, 2 ** (n + 1)):
            mask = bin(i)[3:]
            answer.append([nums[j] for j in range(n) if mask[j] == '1'])

        return self.get_unique(answer)

    @staticmethod
    def get_unique(x):
        output = []
        for i in x:
            sort_i = sorted(i)
            if sort_i not in output:
                output.append(sort_i)
        return output


a = Solution()
print(a.subsets_with_dup([1, 2, 2]))
print()
print(a.subsets_with_dup([0]))
