CLOSING = ')}]>'
CLOSING_PAIRS = {'(': ')', '{': '}', '[': ']', '<': '>'}


def main():
    with open('input.txt') as fp, open('output.txt', 'w') as output:
        for line in fp:
            parStack = []
            for ch in line:
                if ch in CLOSING_PAIRS:
                    parStack.append(CLOSING_PAIRS[ch])
                elif ch in CLOSING:
                    if len(parStack) == 0 or ch != parStack.pop():
                        output.write('false\n')
                        break
            else:
                output.write('true\n' if len(parStack) == 0 else 'false\n')


if __name__ == '__main__':
    main()
