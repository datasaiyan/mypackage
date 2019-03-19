def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    output = items
    for i in range(len(output)):
        for j in range(len(output)-i-1):
            if output[j] > output[j+1]:
                output[j], output[j+1] = output[j+1], output[j]
    return output


def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items)> 1:
        mid_point = len(items)//2

        list1 = merge_sort(items[:mid_point])
        list2 = merge_sort(items[mid_point:])

        i = j = k = 0

        while (len(list1)>i) and (len(list2)>j):
            if list1[i] < list2[j]:
                items[k] = list1[i]
                i += 1
            else:
                items[k] = list2[j]
                j +=1
            k += 1

        while len(list1) > i:
            items[k] = list1[i]
            i += 1
            k += 1

        while len(list2) > j:
            items[k] = list2[j]
            j += 1
            k += 1

    return items


def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items
    else:
        return quick_sort([i for i in items[1:] if i < items[0]]) + [items[0]] + quick_sort([i for i in items[1:] if i >= items[0]])
