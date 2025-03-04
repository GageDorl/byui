def main():
    provinces = readList("provinces.txt")
    provinces.pop(0)
    provinces.pop(-1)

    for i,province in enumerate(provinces):
        if province == "AB":
            provinces[i] = "Alberta"
    print(provinces)
    print(f'Alberta occurs {provinces.count("Alberta")} times in the modified list.')

def readList(filename):
    list = open(filename, "r")
    return list.read().split("\n")

if __name__ == '__main__':
    main()