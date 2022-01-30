def bubble_sort(list):
    ordered_list = list[:]

    while True:
        swapped = False

        for index in range(len(ordered_list) - 1):
            if (ordered_list[index] > ordered_list[index + 1]):
                ordered_list[index], ordered_list[index + 1] = ordered_list[index + 1], ordered_list[index]
                swapped = True    
    
        if not swapped:
            break

    return ordered_list

def merge_sort(list):
    # Verifying if is a atomic value (or is empty)
    if len(list) <= 1:
        return list

    end_index_first_chunk = (len(list) // 2)
    ordered_list_chunk_1 = merge_sort(list[:end_index_first_chunk] )
    ordered_list_chunk_2 = merge_sort(list[end_index_first_chunk:])
    return __merge_sort_merge(ordered_list_chunk_1, ordered_list_chunk_2)

def __merge_sort_merge(list1, list2):
    merged_list = []

    while len(list1) and len(list2):
        if (list1[0] > list2[0]):
            merged_list.append(list2[0])
            list2.pop(0)
        else:
            merged_list.append(list1[0])
            list1.pop(0)

    merged_list.extend(list1)
    merged_list.extend(list2)
    return merged_list

numbers = [1, 4, -3, -2, 10, 8]
numbers_ordered = bubble_sort([1, 4, -3, -2, 10, 8])

print(numbers)
print(numbers_ordered)

numbers = [1, 4, -3, -2, 10, 8]
numbers_ordered = merge_sort([1, 4, -3, -2, 10, 8])

print(numbers)
print(numbers_ordered)
