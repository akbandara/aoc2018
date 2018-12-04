guard_log = {}
guard_id = ''
sleep_time = 0
wake_time = 0

log_entries = open('day4/day4-input.txt', 'r').read().split('\n') # read the input file
log_entries.sort(key=lambda l: l.split(']')[0], reverse=False)

for log_entry in log_entries:
    log_event = log_entry.split('] ')[1]
    log_date = log_entry.split('] ')[0].split(' ')[0][6:11]
    log_minute = log_entry.split('] ')[0].split(' ')[1][3:5]
    if (log_event.startswith('Guard #')):
        guard_id = log_event[7:log_event.index(' ', 7)]
        if guard_id not in guard_log.keys():
            guard_log[guard_id] = {'Sleep Duration':0, 'Sleep Minutes':[0 for min in range(60)]}
    if (log_event.startswith('falls')):
        sleep_time = int(log_minute)
    if (log_event.startswith('wakes')):
        wake_time = int(log_minute) 
        print("Guard #%s fell asleep between %d and %d = %d mins" % (guard_id, sleep_time, wake_time, (wake_time-sleep_time)))
        guard_log[guard_id]['Sleep Duration'] = guard_log[guard_id]['Sleep Duration'] + (wake_time-sleep_time)
        for min in range(sleep_time, wake_time):
            guard_log[guard_id]['Sleep Minutes'][min] = guard_log[guard_id]['Sleep Minutes'][min] + 1

# Find Sleepiest Guard and Highest Frequency Minute for that guard
sleepy_guard=''
max_freq_minute = 0
for guard in guard_log:
    if sleepy_guard not in guard_log:
        sleepy_guard = guard
    if (guard_log[guard]['Sleep Duration'] > guard_log[sleepy_guard]['Sleep Duration']):
        sleepy_guard = guard
        max_sleep = 0
        for min in range(0,59):
            if (guard_log[sleepy_guard]['Sleep Minutes'][min]>max_sleep):
                max_sleep = guard_log[sleepy_guard]['Sleep Minutes'][min]
                max_freq_minute = min

print("**** Sleepiest Guard %s Sleeps most often in minute %d: Checksum -> %d" % (sleepy_guard, max_freq_minute, (int(sleepy_guard)* max_freq_minute)))


# Find Guard with Highest Frequency Minute for that guard
sleepy_guard=''
max_freq_minute = 0
max_sleep = 0
for guard in guard_log:
    if sleepy_guard not in guard_log:
        sleepy_guard = guard
    for min in range(0,59):
        if (guard_log[guard]['Sleep Minutes'][min]>max_sleep):
            max_sleep = guard_log[guard]['Sleep Minutes'][min]
            max_freq_minute = min
            sleepy_guard = guard
    

print("**** Guard with Highest Freq Minute is %s Sleeps on %d days in minute %d: Checksum -> %d" % (sleepy_guard, max_sleep, max_freq_minute, (int(sleepy_guard)* max_freq_minute)))

