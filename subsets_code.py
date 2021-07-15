def subsets(nums):
    '''
	Учитывая целочисленный массив чисел уникальных элементов, 
	верните все возможные подмножества.

	Набор решений не должен содержать повторяющихся подмножеств.
	Верните решение в любом порядке.

	Example 1:

	Input: nums = [1,2,3]
	Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

	Example 2:

	Input: nums = [0]
	Output: [[],[0]]

	'''
    answer = [] 
    n = len(nums) 
        
    for i in range(2 ** n, 2 ** (n + 1)): 
        mask = bin(i)[3:] 
            
        answer.append([nums[j] for j in range(n) if mask[j] == '1'])
    return answer