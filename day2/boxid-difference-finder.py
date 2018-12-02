
def string_diff(string1, string2):
    diff_count = 0
    for i in range(0, len(string1)-1):
        if string1[i] != string2[i]:
            diff_count = diff_count + 1
    return diff_count

data = open('day2-input.txt', 'r').read().split('\n') # read the input file

for box_id1 in data:
    for box_id2 in data:
        #print("Comparing Box IDs: " + box_id1 + " | " + box_id2)
        if string_diff(box_id1, box_id2) == 1:
            print("FOUND Match:")
            print(box_id1)
            print(box_id2)