

if __name__ == "__main__":
    lines = open("input/input2.txt").readlines()

    # Part I
    depth = 0
    horizontal = 0

    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        if lines[i][0] == 'forward':
            horizontal += int(lines[i][1])
        elif lines[i][0] == 'down':
            depth += int(lines[i][1])
        elif lines[i][0] == 'up':
            depth -= int(lines[i][1])
    
    print(horizontal * depth)

    # Part II
    depth = 0
    horizontal = 0
    aim = 0

    for i in range(len(lines)):
        if lines[i][0] == 'forward':
            horizontal += int(lines[i][1])
            depth += int(lines[i][1]) * aim
        elif lines[i][0] == 'down':
            aim += int(lines[i][1])
        elif lines[i][0] == 'up':
            aim -= int(lines[i][1])
    
    print(horizontal * depth)