def get_lattice_path_count(rows, columns):
    end_state = (columns + 1) * (rows + 1)
    paths = 0
    for i in range(0, end_state, 1):
        print('i', i)
    paths += 1
    return paths
    

print(get_lattice_path_count(1, 2))
#  0 1 2 5
#  0 1 4 5
#  0 3 4 5

#  + 1
#  + 3