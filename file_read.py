try:
    fd = open("text.txt")
    print("File opened")
    fd.close()

except FileNotFoundError:
    print("File not found")

with open("text.txt", "r") as fd:
    print(fd.read())

with open("text.txt", "f") as fd:
    for line in fd:
        # print(line)
        # print(line,end="")
        print(line.strip())