original_list = [0, 1, 0, 3, 112]


modified_list = [x for x in original_list if x != 0] + [x for x in original_list if x == 0]

print(f"{modified_list}")

