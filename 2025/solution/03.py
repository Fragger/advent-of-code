import sys


def maxjoltage(bank, enable):
    jolts = 0
    for i in reversed(range(enable)):
        batt = max(int(char) for char in bank[: -1 - i])
        bank = bank[bank.index(str(batt)) + 1 :]
        jolts *= 10
        jolts += batt
    return jolts


p1 = 0
p2 = 0
with open(sys.argv[1] if len(sys.argv) > 1 else "../input/03") as f:
    for line in f:
        p1 += maxjoltage(line, 2)
        p2 += maxjoltage(line, 12)

print(p1)
print(p2)
