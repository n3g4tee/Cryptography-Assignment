from matrix import matrix2bytes

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    x = []
    for i in range(len(s)):
        for j in range(4):
            x.append(s[i][j] ^ k[i][j])
    return [x[i:i+4] for i in range(0, len(x), 4)]

if __name__ == '__main__':
    print("".join(chr(i) for i in matrix2bytes(add_round_key(state, round_key))))

