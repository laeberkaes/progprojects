from sys import stdin

with open("test.txt", "a") as notebook:
    while True:
        inp = stdin.readline()
        if inp.strip() == "END":
            break
        else:
            notebook.write(inp)

for line in open("test.txt").readlines():
    print(line)