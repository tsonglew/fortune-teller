import json


def calculate_value(l):
    l = list(reversed(l))
    mul = 1
    sum = 0
    for i in range(6, 0, -1):
        sum += mul * int(l[i - 1])
        mul *= 2

    return sum


with open("assets/double_divination.txt") as f, open(
    "assets/double_divination.json", "w+"
) as jf:
    result = {"data": []}
    while 1:
        l = f.readline()
        if not l:
            break
        s = l.split()
        result["data"].append(
            {
                "name": s[0],
                "hexagram": s[1],
                "value": calculate_value(s[2].split("#")),
            }
        )
    result["data"].sort(key=lambda x: x["value"])
    jf.write(json.dumps(result))
