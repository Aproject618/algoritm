def twoSum(nums, target):
	'''
	Функция принимает на вход массив целых чисел и одно целое число.
	Задача: учитывая массив целых чисел, найдите два числа, которые 
	складываются в определенное целевое число.

	Given an array of integers nums and an integer target,
	return indices of the two numbers such that they add up to target.
	You may assume that each input would have exactly one solution, 
	and you may not use the same element twice.
	You can return the answer in any order. 

	Example 1:

	Input: nums = [2,7,11,15], target = 9
	Output: [0,1]
	Output: Because nums[0] + nums[1] == 9, we return [0, 1].

	Example 2:

	Input: nums = [3,2,4], target = 6
	Output: [1,2]

	Example 3:

	Input: nums = [3,3], target = 6
	Output: [0,1]

	'''
    cash = {} # Создаем пустой словарь

    for i, num in enumerate(nums):
        if target - num in cash:
        	'''
			Если целевое число - текущее число 
            содержиться в словаре, то 
        	'''
            return [cash[target-num], i] # возвращаем индекс хранящийся в cash и текущий индекс
        cash[num] = i # Добавляем в словарь значение и его индекс
    return [-1, -1] # Если решения нет, возвращаем [-1, -1]