import collections
import bisect

# Part 1
def DFS(v, e, vertex, ordered_list):
  adjacent_vertices = e[vertex]
  for adj in reversed(adjacent_vertices):
    if not v[adj]:
      DFS(v, e, adj, ordered_list)
  v[vertex] = True
  ordered_list.append(vertex)

f  = open("input.txt", "r")
content = f.readlines()
e = collections.defaultdict(list)
e2 = collections.defaultdict(list)
v = collections.defaultdict(bool)
preceded_by_count = collections.defaultdict(int)
ordered_list = []

# Adjacency list
for line in content:
  fst = line[5]
  snd = line[36]
  if v.get(fst) is None:
    e[fst] = []
    e2[fst] = []
    v[fst] = False
    preceded_by_count[fst] = 0
  if v.get(snd) is None:
    e[snd] = []
    e2[snd] = []
    v[snd] = False
    preceded_by_count[snd] = 0
  bisect.insort(e[fst], snd)
  bisect.insort(e2[snd], fst)
  preceded_by_count[snd] += 1

# DFS
for item in sorted(sorted(preceded_by_count.items(), reverse=True), key = lambda i: i[1]):
  vertex = item[0]
  if not v[vertex]:
    DFS(v, e, vertex, ordered_list)

order = "".join(reversed(ordered_list))
print(order)

# Part 2
import string
import numpy as np
alphabet = string.ascii_lowercase.upper()
number_of_workers = 5

# A cache storing the time frame of the end of each task.
parent_latest_list = collections.defaultdict(int)

# A cache storing the different return values of calculate().
cache = np.full((len(order), number_of_workers), -1)

# Returns the duration of a task corresponding to the letter represented by "char".
def get_seconds(char):
  return alphabet.find(char) + 61

# Returns the first time frame task "vertex" can be started.
def get_parent_latest(e2, vertex):
  maxim = 0
  for adj in e2[vertex]:
    num = parent_latest_list[order.find(adj)]
    if num > maxim:
      maxim = num
  return maxim

# Returns the first time frame the worker with index "worker_index" becomes free after the task with index "n" is completed.
def calculate(e2, n, worker_index):
  if cache[n][worker_index] != -1:
    return cache[n][worker_index]
  vertex = order[n]
  
  # Base case.
  if n == 0:
    if worker_index == 0:
      cache[n][worker_index] = get_seconds(vertex)
    parent_latest_list[n] = cache[n][worker_index]
    if worker_index != 0:
      cache[n][worker_index] = 0
    return cache[n][worker_index]
  
  # Calculate the first time frames for each worker.
  earliest_starts_by_worker = []
  for i in range(number_of_workers):
    earliest_starts_by_worker.append(calculate(e2, n - 1, i))
  
  # Arbitrarily large numbers (for finding the minimum).
  worker_earliest_index = number_of_workers + 10
  earliest = float("inf")
  parent_latest_minute = get_parent_latest(e2, vertex)

  for i in range(number_of_workers):
    num = max(earliest_starts_by_worker[i], parent_latest_minute)
    if num < earliest:
      earliest = num
      worker_earliest_index = i

  if worker_index == worker_earliest_index:
    parent_latest_list[n] = earliest + get_seconds(vertex)
    cache[n][worker_index] = earliest + get_seconds(vertex)
  else:
    cache[n][worker_index] = earliest_starts_by_worker[worker_index]
  return cache[n][worker_index]

# Main
maximum_time = 0
for i in range(number_of_workers):
  num = calculate(e2, len(order) - 1, i)
  if maximum_time < num:
    maximum_time = num
print(maximum_time)