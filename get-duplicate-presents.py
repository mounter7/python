# items = [1, 2, 9, 4, 5, 7, 7, 8, 2, 9, 0, 4, 4, 7, 7]
# d = []

# for i in range(len(items)):
#     for j in range(i + 1, len(items)):
#         if items[i] == items[j] and items[i] not in d:
#             d.append(items[i])

# print(d)

def find_duplicates(lst):
    duplicates = []
    seen = set()

    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates

# Example usage
#my_list = [1, 2, 3, 4, 2, 5, 3, 6, 4]
my_list = [1, 2, 9, 4, 5, 7, 7, 8, 2, 9, 0, 4, 4, 7, 7]
duplicates = find_duplicates(my_list)
print(duplicates)
