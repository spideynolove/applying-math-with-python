import random


def generate_numbers(range_=144, sub_=13, change_sign_count=5):
    a = [i for i in range(range_)]
    random.shuffle(a)
    selected_elements = random.sample(a, sub_)

    indices_to_change = random.sample(range(sub_), change_sign_count)
    for idx in indices_to_change:
        selected_elements[idx] = -selected_elements[idx]
    return selected_elements
