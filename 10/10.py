import re

with open('input.txt') as f:
  lines = [l.rstrip('\n') for l in f]
  lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

  smallest = float("inf")
  smallest_ind = float("inf")
  for i in range(20000):
    minx = min(x + i * vx for (x, y, vx, vy) in lines)
    maxx = max(x + i * vx for (x, y, vx, vy) in lines)
    miny = min(y + i * vy for (x, y, vx, vy) in lines)
    maxy = max(y + i * vy for (x, y, vx, vy) in lines)

    if smallest > maxx - minx + maxy - miny:
      smallest = maxx - minx + maxy - miny
      smallest_ind = i
  print(smallest_ind)