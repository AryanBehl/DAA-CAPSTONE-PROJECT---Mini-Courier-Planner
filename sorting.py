def merge_sort(parcels):
    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i]["priority"], -left[i]["deadline"]) > (right[j]["priority"], -right[j]["deadline"]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort_parcels(parcels):
    return merge_sort(parcels)
