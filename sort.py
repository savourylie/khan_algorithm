def swap(lst, index1, index2):
	lst = lst.copy()

	lst[index1], lst[index2] = lst[index2], lst[index1]

	return lst 


def selection_sort(lst):
	lst = lst.copy()

	for i, x in enumerate(lst):
		min_index = i
		for j in range(i, len(lst)):
			if lst[j] < lst[min_index]:
				min_index = j

		lst = swap(lst, i, min_index)
		# lst[i], lst[min_index] = lst[min_index], lst[i]

	return lst


def insertion_sort(lst, result_list=None):
	lst = lst.copy()

	if result_list is None:
		result_list = [lst.pop(0)]

	if len(lst) == 0:
		return result_list

	new_card = lst.pop(0)

	insert = False
	for i in range(len(result_list) - 1, -1, -1):
		if new_card > result_list[i]:
			result_list = result_list[:i + 1] + [new_card] + result_list[i + 1:]
			insert = True
			break

	if not insert:
		result_list = [new_card] + result_list

	return insertion_sort(lst, result_list=result_list)



def quick_sort(lst):
	if len(lst) < 2:
		return lst

	pivot = lst[0]
	equals = [x for x in lst if x == pivot]
	smallers = [x for x in lst if x < pivot]
	largers = [x for x in lst if x > pivot]

	return quick_sort(smallers) + equals + quick_sort(largers)


def __merge_sorted(lst1, lst2):
	lst1, lst2 = lst1.copy(), lst2.copy()

	if len(lst1) == 0:
		return lst2

	if len(lst2) == 0:
		return lst1

	result_list = []

	elt1, elt2 = None, None

	while (len(lst1) != 0 or len(lst2) != 0) or (elt1 is not None or elt2 is not None):

		if elt1 is None:
			try:
				elt1 = lst1.pop(0)
			except IndexError:
				if elt2 is not None:
					return result_list + [elt2] + lst2
				else:
					return result_list + lst2

		if elt2 is None:
			try:
				elt2 = lst2.pop(0)
			except IndexError:
				if elt1 is not None:
					return result_list + [elt1] + lst1
				else:
					return result_list + lst1

		if elt1 == min(elt1, elt2):
			result_list.append(elt1)
			elt1 = None

		else:
			result_list.append(elt2)
			elt2 = None

	return result_list

def merge_sort(lst):
	if len(lst) < 2:
		return lst

	mid_index = len(lst) // 2

	left = merge_sort(lst[:mid_index])
	right = merge_sort(lst[mid_index:])

	return __merge_sorted(left, right)


def __test_merge_sorted():
	test_list_sorted = __merge_sorted(test_list, test_list2)

	assert test_list_sorted == sorted(test_list + test_list2)
	print("__merge_sorted passed.")


def __test_merge_sort():
	test_list_sorted = merge_sort(test_list)
	assert test_list_sorted == sorted(test_list)
	print("merge_sort passed.")	

def __test_selection_sort():
	test_list_sorted = selection_sort(test_list)

	assert test_list_sorted == sorted(test_list)

	print("selection_sort passed.")


def __test_insertion_sort():
	test_list_sorted = insertion_sort(test_list)

	assert test_list_sorted == sorted(test_list)

	print("insertion_sort passed.")


def __test_quick_sort():
	test_list_sorted = quick_sort(test_list)
	assert test_list_sorted == sorted(test_list)
	print("quick_sort passed.")

if __name__ == '__main__':
	# test_list = [1, 1, 8, 9, 4, 5, 6, 8]

	import random
	import time

	test_list = random.sample(range(1, 100), 5)
	test_list2 = random.sample(range(1, 100), 5)
	# test_list = [1, 3, 5, 9, 10, 11, 143]
	# test_list2 = [2, 4, 6, 8, 12]

	# __test_merge_sorted()
	__test_selection_sort()
	__test_insertion_sort()
	__test_quick_sort()
	__test_merge_sort()

