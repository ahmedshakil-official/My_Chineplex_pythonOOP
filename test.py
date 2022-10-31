ll = [(3, 1), (2, 2), (1, 0)]

d = {"A": [[0, 1, 2, 3], [2, 4, 7], [0, 1, 2, 3], [2, 4, 7], [0, 1, 2, 3], [2, 4, 7]]}

for i in ll:
    for key, value in d.items():
        if value[i[0]][i[1]] != 'X':
            print(value[i[0]][i[1]])
