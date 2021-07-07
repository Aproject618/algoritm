def quicksort(array):
	'''
	Функция принимает на вход массив array, возращает отсортированный массив.
	Сортировка выполняется методом быстрой сортировки quicksort.
	'''
	if len(array) < 2:
		return array # Базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
	else:
		pivot = array[0] # Опорный элемент
		
		less = [i for i in array[1:] if i <= pivot] # Подмассив всех элементов, меньших опорного

		greater = [i for i in array[1:] if i > pivot] # Подмассив всех элементов, больших опорного

		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))		 