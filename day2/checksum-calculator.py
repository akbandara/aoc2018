import collections

freq2_boxid_count = 0
freq3_boxid_count = 0

# returns true if a character in 'word' occurs with given freq
def check_char_freq(word, freq):
    char_counts = collections.Counter(word)
    return (freq in char_counts.values())

data = open('day2-input.txt', 'r').read().split('\n') # read the input file

for line in data:
    if check_char_freq(line, 2):
        print("BoxID Freq 2 = " + line)
        freq2_boxid_count = freq2_boxid_count + 1
        
    if check_char_freq(line, 3):
        print("BoxID Freq 3 = " + line)
        freq3_boxid_count = freq3_boxid_count + 1

print ("Num Freq 2 BoxIDs = " + str(freq2_boxid_count))
print ("Num Freq 3 BoxIDs = " + str(freq3_boxid_count))
print ("Checksum = " + str(freq2_boxid_count*freq3_boxid_count))

