import numpy as np


def original_function(vector_null, vector_unit, arg):
    func_vec = []
    arg = int(arg)
    l_vector_null = list(vector_null)
    l_vector_unit = list(vector_unit)
    new_vector_null = np.array_split(l_vector_null, (2 ** arg) // 2)
    new_vector_unit = np.array_split(l_vector_unit, (2 ** arg) // 2)
    for i in range(2 ** arg):
        if i % 2 != 0:
            func_vec.extend(new_vector_null[i // 2])
        else:
            func_vec.extend(new_vector_unit[i // 2])
    return ''.join(func_vec)


print(original_function('0o01111110', 0, 2))
