with open("day3.txt", "r+") as f:
    prompt = f.readlines()

for line in prompt:
    p1 = line.strip().split("mul(")
    for val in p1:
        print(f"{val=}")
        p2 = val.split(")")
        print(f"{p2=}")
