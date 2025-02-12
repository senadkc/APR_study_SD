print("deneme")
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        for item in list2:
            common_elements.append(item)
    return common_elements

list1 = [2, 4, 6, 8]
list2 = [4, 8, 10, 12]
result = find_common_elements(list1, list2)
print("deneme")
print("deneme")