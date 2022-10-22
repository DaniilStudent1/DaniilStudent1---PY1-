list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
ind = 0
maximum = list_numbers[ind]
for i, R in enumerate(list_numbers):
    if R > maximum:
        maximum = R
        ind = i

list_numbers[ind], list_numbers[-1] = list_numbers[-1], list_numbers[ind]
print(list_numbers)