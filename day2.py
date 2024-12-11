import numpy as np


def is_safe(arr):
    diff = np.diff(arr)
    out_of_bounds = np.all(np.abs(diff) <= 3)
    increasing = np.all(diff > 0)
    decreasing = np.all(diff < 0)

    return out_of_bounds and (increasing or decreasing)


with open("day2.txt", "r+") as f:
    prompt = f.readlines()

num_safe = 0
for line in prompt:
    data = np.array(line.strip().split(), dtype=np.int64)
    num_vals = data.shape[0]
    safe = is_safe(data)
    if safe:
        num_safe += 1
    else:
        for i in range(num_vals):
            arr = np.delete(data, i)
            safe = is_safe(arr)
            if safe:
                num_safe += 1
                break


print(num_safe)
