import re

# Part I
def drawFirst(drawOrder, boards, nBoards):
    win = False
    for num in drawOrder:
        for i in range(nBoards):
            for j in range(5):
                if num in boards[i]['rows'][j]:
                    boards[i]['rows'][j].remove(num)
                    if len(boards[i]['rows'][j]) == 0:
                        win = True
                if num in boards[i]['cols'][j]:
                    boards[i]['cols'][j].remove(num)
                    if len(boards[i]['cols'][j]) == 0:
                        win = True
            if win:
                sumUnmarked = 0
                for j in range(5):
                    for elem in boards[i]['rows'][j]:
                        sumUnmarked += elem
                return sumUnmarked * num
    return -1

# Part II
def drawLast(drawOrder, boards, nBoards):
    win = set()
    for num in drawOrder:
        for i in range(nBoards):
            if i not in win:
                for j in range(5):
                    if num in boards[i]['rows'][j]:
                        boards[i]['rows'][j].remove(num)
                        if len(boards[i]['rows'][j]) == 0:
                            win.add(i)
                    if num in boards[i]['cols'][j]:
                        boards[i]['cols'][j].remove(num)
                        if len(boards[i]['cols'][j]) == 0:
                            win.add(i)
                if len(win) == nBoards:
                    sumUnmarked = 0
                    for j in range(5):
                        for elem in boards[i]['rows'][j]:
                            sumUnmarked += elem
                    return sumUnmarked * num
    return -1

if __name__ == "__main__":
    file = open("input/input4.txt")
    drawOrder = list(map(lambda x : int(x), file.readline().split(',')))

    line = file.readline()
    boards = []
    nBoards = 0
    while nBoards < 100:
        boards  += [{'rows':[set() for _ in range(5)], 'cols':[set() for _ in range(5)] }]
        for i in range(5):
            line = file.readline()
            nums = list(map(lambda x : int(x), re.findall(r'\w+', line)))
            for j in range(5):
                boards[nBoards]['rows'][i].add(nums[j])
                boards[nBoards]['cols'][j].add(nums[j])
        nBoards += 1
        file.readline()

    print(drawFirst(drawOrder, boards, nBoards))

    print(drawLast(drawOrder, boards, nBoards))
