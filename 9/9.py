from collections import deque

f  = open("input.txt", "r")
content = f.read().split("; ")
number_of_players = int(content[0].split(" ")[0])
marble_points = int(content[1].split(" ")[4])

players = ([0] * number_of_players)
circle = deque([0])
current_index = 0
for i in range(1, marble_points + 1):
  if i % 23 != 0:
    circle.rotate(-1)
    circle.append(i)
  else:
    current_player = (i % number_of_players) - 1
    players[current_player] += i
    circle.rotate(7)
    players[current_player] += circle.pop()
    circle.rotate(-1)

print(max(players))