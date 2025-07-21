# Replace Items

lst = [1, 2, 3, 4, 5, 6, 7, 8]
element_2 = lst.pop(1)
lst.insert(2,element_2)
print(lst)  # [1, 3, 2, 4, 5]

element_8 = lst.pop()
print(element_8)
lst.insert(0, element_8)
print(lst)
element_1 = lst.pop(1)
lst.append(element_1)
print(lst)


