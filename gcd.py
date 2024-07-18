def main():
    a, b = [int(x) for x in input('(a b)>').split()]
    print(step(a, b))


def step(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a > b:
        return step(a % b, b)
    else:
        return step(a, b % a)


if __name__ == '__main__':
    main()
