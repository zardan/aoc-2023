file = open("input")
[times, distances] = file.read().split("\n")
times = times[9:].split(" ")
times = [int(t) for t in times if len(t)>0]
distances = distances[9:].split(" ")
distances = [int(d) for d in distances if len(d)>0]

def dist(total_time, powerup_time):
    return (total_time-powerup_time)*powerup_time

# PART ONE

key = 1
for time, record in zip(times, distances):
    button_durations = list(range(0,time+1))
    distances_for_duration = [dist(time, d) for d in button_durations]
    wins = sum(1 for d in distances_for_duration if d > record)
    key *= wins

print("PART 1.", key)

# PART TWO

race_time = int("".join([str(t) for t in times]))
record = int("".join([str(d) for d in distances]))

t_min = 0
t_max = int((race_time+1)/2)
while abs(t_min-t_max)>1:
    t_mid = int((t_min+t_max)/2)
    d_mid = dist(race_time, t_mid)
    if d_mid > record: 
        t_max = t_mid
    else: 
        t_min = t_mid

wins = race_time+1-2*t_max

print("PART 2.", wins)