import numpy as np
import random


def generate_numbers(range_=144, sub_=13, change_sign_count=5, etype='int', precision=1):
    a = [i for i in range(range_)]
    random.shuffle(a)
    selected_elements = random.sample(a, sub_)

    indices_to_change = random.sample(range(sub_), change_sign_count)
    for idx in indices_to_change:
        selected_elements[idx] = -selected_elements[idx]

    if etype == 'float':
        selected_elements = [round(float(num) + random.uniform(-0.5, 0.5), precision) for num in selected_elements]
    elif etype == 'int':
        selected_elements = [int(num) for num in selected_elements]
    else:
        raise ValueError("etype must be 'float' or 'int'")

    return selected_elements


def make_shape(processed_list, shape=(3, 3)):
    return np.array(processed_list).reshape(shape).tolist()
