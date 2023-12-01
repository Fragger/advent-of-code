
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 

with open('../input/01', 'r') as f:
    p1sum = 0
    p2sum = 0
    for line in f:
        p1digits = []
        p2digits = []
        for i, char in enumerate(line):
            if char.isdigit():
                p1digits.append(char)
                p2digits.append(char)
            else:
                for j, digit in enumerate(digits):
                    if line[i:].startswith(digit):
                        p2digits.append(str(j+1))
                        break
        p1sum += int(p1digits[0] + p1digits[-1])
        p2sum += int(p2digits[0] + p2digits[-1])

    print(f'{p1sum=}')
    print(f'{p2sum=}')
