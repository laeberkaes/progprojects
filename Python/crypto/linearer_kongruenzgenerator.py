a = 7141
b = 54773
m = 259200


def kongr(n):
    if n > 0:
        return (a * kongr(n - 1) + b) % m
    else:
        return (a * 0 + b) % m


def neumann(bin):
    b1 = "0" * (32 - len(bin[2:])) + bin[2:]
    b2 = []

    for i in range(0, 32, 2):
        if b1[i:i + 2] == "01":
            b2.append("0")
        elif b1[i:i + 2] == "10":
            b2.append("1")

    return "".join(b2)


for i in range(20):
    print("0" * (32 - len(bin(kongr(i))[2:])) + bin(kongr(i))[2:])
    print(neumann(bin(kongr(i))))
