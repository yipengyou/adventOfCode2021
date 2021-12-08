codes = []
shown = []

letters = "abcdefg"

correct = ["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]

with open("day8_inputs.txt", 'r') as f:
    for line in f:
        codes += [line.strip().split("|")[0].split(" ")[:-1]]
        shown += [line.strip().split("|")[1].split(" ")]

# print(codes[0])
print(shown[0])

lettercodes = {74: 'a', 100: 'b', 23: 'c', 12: 'd', 32: 'e', 87: 'f', 72: 'g'}

def decode(code):
    dictionary = {}
    sets = [""] * 8

    for word in code:
        sets[len(word)] += word
    sets5 = [""] * 4
    for letter in letters:
        sets5[sets[5].count(letter)] += letter
    sets6 = [""] * 4
    for letter in letters:
        sets6[sets[6].count(letter)] += letter

    decoding = [""] * 7
    decoding[0] = sets[2]
    decoding[1] = sets[3]
    decoding[2] = sets[4]
    decoding[3] = sets5[3]
    decoding[4] = sets5[2]
    decoding[5] = sets5[1]
    decoding[6] = sets6[3]

    for letter in letters:
        n = 0
        for i in range(7):
            if letter in decoding[i]:
                n += 2**i
        dictionary[letter] = lettercodes[n]

    return dictionary

print(decode(codes[0]))

def getnumbers(code, shown):
    d = decode(code)
    display = []
    for word in shown:
        decoded = []
        for letter in word:
            decoded += [d[letter]]
        s = ""
        for letter in sorted(decoded):
            s += letter
        # print(f"Word {word}, decoded {s}, str = {s}")
        display += [correct.index(s)]
    
    return display

print(f"shown[0] = {shown[0][1:]}")
countunique = 0
total = 0
for i in range(len(codes)):
    displaynumbers = getnumbers(codes[i], shown[i][1:])
    n = sum(10**i * displaynumbers[3 - i] for i in range(4))
    print(f"Display {i} : {displaynumbers} :  {n}")
    total += n
    countunique += displaynumbers.count(1)
    countunique += displaynumbers.count(4)
    countunique += displaynumbers.count(7)
    countunique += displaynumbers.count(8)

print(countunique)
print(total)