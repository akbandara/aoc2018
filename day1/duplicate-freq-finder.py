freq = 0
past_freq = {0}

while True:
    data = open('day1-input.txt', 'r').read().split('\n') # read the file
    for line in data: # files are iterable
        freq = freq + int(line)
        #print("Adjusted Frequency by: " + str(int(line)) + " | New Freq = " + str(freq))
        if (freq not in past_freq):
            past_freq.add(freq)
        else:
            print("Duplicate Frequency Found! = " + str(freq))
            exit()
