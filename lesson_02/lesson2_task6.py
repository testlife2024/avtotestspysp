lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
new_lst = []
for i in lst:
    if i < 30 and i % 3 == 0:
        new_lst.append(i)

print(new_lst)