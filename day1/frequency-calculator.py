freq = 0

data = open('day1-input.txt', 'r').read().split('\n') # read the file
for line in data: # files are iterable
    freq = freq + int(line)
    print("Adjusted Frequency by: " + str(int(line)) + " | New Freq = " + str(freq))