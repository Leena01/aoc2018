# Part 1
import sys
sys.setrecursionlimit(20000)
f  = open("input.txt", "r")
content = [int(x) for x in f.read().split(" ")]

def process(content, i):
  child_count = content[i]
  i += 1
  metadata_count = content[i]

  sum_of_metadata = 0
  for j in range(child_count):
    i += 1
    tmp, i = process(content, i)
    sum_of_metadata += tmp
  for j in range(metadata_count):
    i += 1
    sum_of_metadata += content[i]
  return sum_of_metadata, i

# Main.
i = 0
total = 0
length = len(content)
while i < length - 1:
  tmp, i = process(content, i)
  total += tmp
print(total)

# Part 2
def get_value(content, i):
  child_count = content[i]
  i += 1
  metadata_count = content[i]
  
  # No child nodes.
  if child_count == 0:
    sum_of_metadata = 0
    for j in range(metadata_count):
      i += 1
      sum_of_metadata += content[i]
    return sum_of_metadata, i

  # One or more child nodes.
  values = []
  value = 0
  for j in range(child_count):
    i += 1
    tmp, i = get_value(content, i)
    values.append(tmp)
  for j in range(metadata_count):
    i += 1
    if content[i] > 0 and content[i] <= child_count:
      value += values[content[i] - 1]
  return value, i

# Main.
value = 0
i = 0
while i < length - 1:
  tmp, i = get_value(content, i)
  value += tmp
print(value)