

if __name__ == "__main__":
    lines = open("input/input1.txt").readlines()

    # Part I
    previous = 9999
    count = 0
    for i in range(len(lines)):
        lines[i] = int(lines[i])
        if lines[i] > previous:
            count += 1
        previous = lines[i]
    print(count)

    # Part II
    previous = 999999
    count = 0
    for i in range(len(lines) - 2):
        current = lines[i] + lines[i+1] + lines[i+2]
        if current > previous:
            count += 1
        previous = current
    print(count)
