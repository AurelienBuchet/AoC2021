

if __name__ == "__main__":
    lines = open("input/input3.txt").readlines()

    # Part I

    binSize = len(lines[0])-1
    rates = [0 for _ in range(binSize)]

    for line in lines:
        for i in range(binSize):
            if line[i] == '1':
                rates[i] += 1
    gamma = ""
    epsilon = ""
    for i in range(len(rates)):
        if rates[i] > len(lines) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma,2) * int(epsilon, 2))

    # Part II

    oxygenRates = [0 for _ in range(binSize)]
    oxygenNumbers = [l for l in lines]
    oxygenRating = 0

    CO2Rates = [0 for _ in range(binSize)]
    CO2Numbers = [l for l in lines]
    CO2Rating = 0

    for i in range(binSize):
        oxygenRates = [0 for _ in range(binSize)]
        for num in oxygenNumbers:
            if num[i] == '1':
                oxygenRates[i] += 1
        if oxygenRates[i] >= len(oxygenNumbers) / 2:
            oxygenNumbers = [n for n in oxygenNumbers if n[i] == '1']
        else:
            oxygenNumbers = [n for n in oxygenNumbers if n[i] == '0']
        if len(oxygenNumbers) == 1:
            oxygenRating = oxygenNumbers[0]
            break

    for i in range(binSize):
        CO2Rates = [0 for _ in range(binSize)]
        for num in CO2Numbers:
            if num[i] == '1':
                CO2Rates[i] += 1
        if CO2Rates[i] >= len(CO2Numbers) / 2:
            CO2Numbers = [n for n in CO2Numbers if n[i] == '0']
        else:
            CO2Numbers = [n for n in CO2Numbers if n[i] == '1']
        if len(CO2Numbers) == 1:
            CO2Rating = CO2Numbers[0]
            break    
    print(int(oxygenRating,2) * int(CO2Rating,2))
