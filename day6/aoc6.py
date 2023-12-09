# Parprogrammering mellan älskling och älskling
# Båda lovar att hålla gott humör och inte börja sucka/skrika åt varandra
# Båda älskar varandra och uppskattar varandras olikheter

file = open("input")
[times, distances] = file.read().split("\n")
times = times[9:].split(" ")
times = [int(t) for t in times if len(t)>0]
distances = distances[9:].split(" ")
distances = [int(d) for d in distances if len(d)>0]

key = 1
for time, record in zip(times, distances):
    button_durations = list(range(0,time+1))
    distances = [(time-d)*d for d in button_durations]
    wins = sum(1 for d in distances if d > record)
    key *= wins

print("Part1:", key)