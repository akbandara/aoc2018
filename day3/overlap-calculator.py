
fabric = [['.' for i in range(1000)] for j in range(1000)]
overlapping_area = 0
nonoverlapping_claim_id = ''

claims = open('day3/day3-input.txt', 'r').read().split('\n') # read the input file

# Process Claims and build model of fabric where . = unclaimed, o = claimed, x = overlap
for claim_string in claims:
    #parse the claim string to get parameters of the rectangle
    claim_id = claim_string.split('@')[0]
    start_x = int(claim_string.split('@')[1].split(':')[0].split(',')[0])
    start_y = int(claim_string.split('@')[1].split(':')[0].split(',')[1])
    end_x = start_x + int(claim_string.split('@')[1].split(':')[1].split('x')[0])
    end_y = start_y + int(claim_string.split('@')[1].split(':')[1].split('x')[1])

    #print ("Processing Claim (%s): (%d,%d)-(%d,%d)" % (claim_id, start_x, start_x, end_x, end_y))

    for x in range(start_x,end_x):
        for y in range(start_y,end_y):
            if (fabric[y][x]=='.'):
                fabric[y][x] = 'o'
            elif (fabric[y][x]=='o'):
                fabric[y][x] = 'x'
                overlapping_area = overlapping_area +1

print ("Overlapping Area = %d" % overlapping_area)

# Check through claims to find instance where there are no 'x's in the claimed area
for claim_string in claims:
    #parse the claim string to get parameters of the rectangle
    claim_id = claim_string.split('@')[0]
    start_x = int(claim_string.split('@')[1].split(':')[0].split(',')[0])
    start_y = int(claim_string.split('@')[1].split(':')[0].split(',')[1])
    end_x = start_x + int(claim_string.split('@')[1].split(':')[1].split('x')[0])
    end_y = start_y + int(claim_string.split('@')[1].split(':')[1].split('x')[1])

    #print ("Checking Claim (%s): (%d,%d)-(%d,%d)" % (claim_id, start_x, start_x, end_x, end_y))
    overlapping_area = sum(x.count('x') for x in [row[start_x:end_x] for row in fabric[start_y:end_y]])
    if (overlapping_area==0):
        nonoverlapping_claim_id = claim_id

print("NON OVERLAPPING CLAIM: %s" % nonoverlapping_claim_id)


