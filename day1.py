import numpy as np
from collections import Counter

with open("day1.txt", "r+") as f:
    prompt = f.readlines()

l_arr = []
r_arr = []
for line in prompt:
    data = line.strip().split("   ")
    l_arr.append(int(data[0]))
    r_arr.append(int(data[1]))

l_arr = np.sort(np.array(l_arr))
r_arr = np.sort(np.array(r_arr))
part1 = np.sum(np.abs(l_arr - r_arr))

r_counts = dict(Counter(r_arr))

sim_score = 0
for i in range(l_arr.shape[0]):
    sim_score += l_arr[i] * r_counts.get(l_arr[i], 0)

print(sim_score)
