def main():
    nStairs = int(input('Number of stairs> '))
    assert(nStairs > 0)
    if nStairs == 1:
        print(1)    # exception
    else:
        numberOfWays = [1, 2] + [0] * (nStairs - 2)
        for step in range(2, nStairs):
            numberOfWays[step] = numberOfWays[step - 1] + numberOfWays[step - 2]
        print(numberOfWays[-1])


if __name__ == '__main__':
    main()
