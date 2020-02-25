import collections

f  = open("input.txt", "r")
content = f.readlines()
content = [(x.strip().split("] ")[0][1:], x.strip().split("] ")[1]) for x in content]
content.sort(key=lambda tup: tup[0])

d = collections.defaultdict(list)
latest_guard = 0
latest_start = 0
for line in content:
  date = line[0].split(" ")
  minute = int(date[1].split(":")[1])
  if line[1] == "wakes up":
    for i in range(latest_start, minute):
      d[latest_guard][i] += 1
  elif line[1] == "falls asleep":
    latest_start = minute
  else:
    latest_guard = int(line[1].split(" ")[1][1:])
    if d.get(latest_guard) is None:
      d[latest_guard] = ([0] * 60)

max_guard_id = -1
max_sum = -1
most_frequent_minute = -1
for i in d.items():
  if max_sum < sum(i[1]):
    max_sum = sum(i[1])
    max_guard_id = i[0]
    most_frequent_minute = i[1].index(max(i[1]))

print(max_guard_id * most_frequent_minute)
  